import matplotlib.pyplot as plt
import numpy as np
import cv2
from rich import print
from functools import lru_cache
import os
from rich.console import Console
from id_manual_tools.matplotlib_gui import matplotlib_gui
import shutil

console = Console()


class manual_tracker(matplotlib_gui):
    def __init__(
        self,
        video_path,
        traj_path,
        ignore_Existing_session=False,
    ):
        self.traj_path = os.path.abspath(traj_path)
        self.video_path = os.path.abspath(video_path)
        self.cap = cv2.VideoCapture(video_path)
        self.total_frames = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
        print(f"Loaded {self.video_path}")

        corrected_path = self.traj_path[:-4] + "_corrected.npy"
        if not os.path.exists(corrected_path) or ignore_Existing_session:
            print(f"Duplicating {self.traj_path} to {corrected_path} ")
            shutil.copyfile(self.traj_path, corrected_path)
        self.traj_path = corrected_path
        self.data = np.load(self.traj_path, allow_pickle=True).item()
        print(f"Loaded {self.traj_path}")

        self.setup_points = {}
        for name, points in self.data["setup_points"].items():
            print(f'Found setup points "{name}" of {len(points)} points')
            self.setup_points[name] = [list(points[:, 0]), list(points[:, 1])]

        self.name = console.input(
            "Enter the name of the setup points to modify/create: "
        )

        if not self.name in self.setup_points:
            self.setup_points[self.name] = [[], []]

        self.xmax = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.ymax = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        self.x_center = self.xmax / 2
        self.y_center = self.ymax / 2

        self.actual_plotted_frame = -1

        self.create_figure()

        console.rule(f"[bold red]Adding_setup points: {self.name}")

        self.frame = 0

        self.set_ax_lims(do_not_draw=True)

        self.draw_frame()
        plt.show()

    def draw_frame(self):

        if self.frame != self.actual_plotted_frame:
            self.im.set_data(self.get_frame(self.frame))

            self.text.set_text(f"Frame {self.frame}")
            self.actual_plotted_frame = self.frame

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def create_figure(self):

        super().__init__("Setup points editor")

        self.im = self.ax.imshow(
            [[[0, 0, 0]]],
            extent=(
                0,
                self.xmax,
                self.ymax,
                0,
            ),
            interpolation="none",
            animated=True,
        )

        self.lines = {
            name: self.ax.plot(*self.close_line(*xy), ":.", label=name)[0]
            for name, xy in self.setup_points.items()
        }
        self.ax.legend()

        self.text = self.ax.text(
            0.1, 0.1, "", size=15, transform=self.ax.transAxes, zorder=15
        )

    @staticmethod
    def close_line(x, y):
        if len(x) < 3:
            return x, y
        else:
            return x + [x[0]], y + [y[0]]

    def key_a(self):
        self.frame = max(0, self.frame - 1)
        self.draw_frame()

    def key_d(self):
        self.frame = min(self.total_frames - 1, self.frame + 1)
        self.draw_frame()

    def key_left(self):
        self.key_a()

    def key_right(self):
        self.key_d()

    def key_w(self):
        out_dict = {}
        for name, points in self.setup_points.items():
            out_dict[name] = np.array(points).astype(int).T
        self.data["setup_points"] = out_dict
        out_path = self.traj_path[:-4] + "_corrected.npy"
        np.save(out_path, self.data)
        print(f"[green]Data saved to {out_path}")

    def key_enter(self):
        self.key_w()
        plt.close()

    @lru_cache(maxsize=20)
    def get_frame(self, frame):

        if self.cap.get(cv2.CAP_PROP_POS_FRAMES) != frame:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame)
        ret, image = self.cap.read()
        assert ret

        return image

    @staticmethod
    def closest_point(x, y, xs, ys):
        distances = [(x - x_i) ** 2 + (y - y_i) ** 2 for x_i, y_i in zip(xs, ys)]
        return np.argmin(distances), np.min(distances)

    @staticmethod
    def sort_points(x, y):

        atan2 = np.arctan2(y - np.mean(y), x - np.mean(x))
        x = [
            (x_i[1], x_i[2])
            for x_i in sorted(zip(atan2, x, y), key=lambda pair: pair[0])
        ]
        return list(map(list, zip(*x)))

    def button_1(self, event):
        self.setup_points[self.name][0].append(event.xdata)
        self.setup_points[self.name][1].append(event.ydata)
        self.setup_points[self.name] = self.sort_points(*self.setup_points[self.name])

        self.lines[self.name].set_data(*self.close_line(*self.setup_points[self.name]))
        self.draw_frame()

    def button_3(self, event):

        point_id, dist = self.closest_point(
            event.xdata, event.ydata, *self.setup_points[self.name]
        )
        if dist < 1000:
            self.setup_points[self.name][0].pop(point_id)
            self.setup_points[self.name][1].pop(point_id)
            self.lines[self.name].set_data(
                *self.close_line(*self.setup_points[self.name])
            )
            self.draw_frame()


def rename_setup_point(traj_path, ignore_Existing_session=False):
    traj_path = os.path.abspath(traj_path)

    modified_path = traj_path[:-4] + "_corrected.npy"
    if os.path.exists(modified_path) and not ignore_Existing_session:
        data = np.load(modified_path, allow_pickle=True).item()
        print(f"Loaded {modified_path}")
    else:
        data = np.load(traj_path, allow_pickle=True).item()
        print(f"Loaded {traj_path}")

    for name, points in data["setup_points"].items():
        print(f'Found setup points "{name}" of {len(points)} points')

    old_name = console.input(f"Enter the OLD name of the setup points: ")
    if old_name in data["setup_points"]:

        new_name = console.input(f'Enter the NEW name for setup points "{old_name}": ')
        data["setup_points"][new_name] = data["setup_points"].pop(old_name)
        console.rule(f'[green]Succesfully renamed points "{old_name}" to "{new_name}"')

        np.save(modified_path, data)
        print(f"[green]Data saved to {modified_path}")

    else:
        print(f'[red]No setup points named "{old_name}", aborting...')


def view_existing_setup_points(data_path, ignore_Existing_session=False):
    data_path = os.path.abspath(data_path)

    modified_path = data_path[:-4] + "_corrected.npy"
    loaded_path = (
        modified_path
        if os.path.exists(modified_path) and not ignore_Existing_session
        else data_path
    )

    data = np.load(loaded_path, allow_pickle=True).item()
    print(f"Loaded {loaded_path}")
    if not isinstance(data["setup_points"], dict):
        data["setup_points"] = {}

    out_path = data_path[:-4] + "_corrected.npy"
    np.save(out_path, data)
    print(f"[green]Data with empty dict saved to {out_path}")

    for name, points in data["setup_points"].items():
        print(f'Found setup points "{name}" of {len(points)} points')


def main(video_path, data_path):

    view_existing_setup_points(data_path)
    while True:
        what_to_do = console.input(
            "[blue]What do you rant to do, rename an existing setup points (r), modify an existing setup points (m), cerate a new one (c), viwe existing setup points (v) or quitting (q)? "
        )
        if what_to_do == "q":
            print("[red]Exitting...")
            return
        elif what_to_do == "r":
            rename_setup_point(data_path)
        elif what_to_do == "v":
            view_existing_setup_points(data_path)
        elif what_to_do in ("m", "c"):
            manual_tracker(
                video_path,
                data_path,
                ignore_Existing_session=False,
            )
        else:
            print(f'[red]Unknown answer "{what_to_do}", please enter a valid answer')


def request_setup_points(video_path, data_path, request=None):

    view_existing_setup_points(data_path)
    while True:
        what_to_do = console.input(
            "[blue]What do you rant to do, rename an existing setup points (r), modify an existing setup points (m), cerate a new one (c), viwe existing setup points (v) or quitting (q)? "
        )
        if what_to_do == "q":
            print("[red]Exitting...")
            return
        elif what_to_do == "r":
            rename_setup_point(data_path)
        elif what_to_do == "v":
            view_existing_setup_points(data_path)
        elif what_to_do in ("m", "c"):
            manual_tracker(
                video_path,
                data_path,
                ignore_Existing_session=False,
            )
        else:
            print(f'[red]Unknown answer "{what_to_do}", please enter a valid answer')


if __name__ == "__main__":
    main(
        video_path="/media/jordi/Fish_videos_LaCie/Videos_20220621_(n=2)/GX010165.MP4",
        data_path="/home/jordi/drive-download-20220704T131649Z-001/Videos_20220621_(n=2)/20220621_0165.npy",
    )
