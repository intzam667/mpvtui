import os
import subprocess
from pathlib import Path
from textual.app import App, ComposeResult
from textual.containers import Center, Container
from textual.widgets import Header, Footer, ListView, ListItem, Button, Static


class VideoManagerApp(App):
    CSS = """
    ListView {
        border: solid white;
        padding: 1;
        width: 80%;
        height: 50vh;
        overflow-y: scroll;
    }
    ListItem {
        background: black;
        margin: 0 0 1 0;
    }
    Button:hover {
        background: blue;
    }
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.video_dir = Path.cwd()
        self.videos = []

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Center(Container(self.create_list_view(), Static("Press Enter to play a video!")))

    def create_list_view(self):
        self.video_list = ListView()
        return self.video_list

    async def on_mount(self):
        self.title = "IntZam's MPV TUI"
        self.videos = [
            f for f in self.video_dir.iterdir() if f.is_file() and f.suffix.lower() in [".mp4", ".mkv", ".avi", ".mov"]
        ]
        for video in self.videos:
            safe_id = video.name.replace(" ", "_").replace("/", "_").replace("\\", "_").replace(":", "_")
            safe_id = ''.join([c if c.isalnum() or c in ['_', '-'] else '_' for c in safe_id])
            self.video_list.append(ListItem(Button(video.name, id=safe_id, name=str(video))))

    async def on_button_pressed(self, event: Button.Pressed):
        video_path = Path(event.button.name)
        if video_path.exists():
            self.play_video(str(video_path))
        else:
            self.log(f"Video path not found: {video_path}")

    def play_video(self, video_path: str):
        try:
            subprocess.run(["mpv", "--quiet", "--no-terminal", "--log-file=/dev/null", "--ao=pulse", video_path], check=True)
        except FileNotFoundError:
            self.log("MPV player not found. Make sure it is installed and in your PATH.")
        except subprocess.CalledProcessError as e:
            self.log(f"Failed to play video: {e}")


if __name__ == "__main__":
    VideoManagerApp().run()
