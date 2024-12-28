import os
import subprocess
from pathlib import Path
from textual.app import App, ComposeResult
from textual.containers import Center, Container
from textual.widgets import Header, Footer, ListView, ListItem, Button, Static, Input


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
    Input {
        background: black;
        color: white; 
        }
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.video_dir = Path.cwd()
        self.videos = []
        self.filtered_videos = []
        self.selected_video = None
        self.rename_input = None
        self.search_input = None
        self.is_renaming = False

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Center(Container(self.create_search_input(), self.create_list_view(), Static("Press Enter to play a video!")))

    def create_list_view(self):
        self.video_list = ListView()
        return self.video_list

    def create_search_input(self):
        self.search_input = Input(placeholder="Search videos...", id="search-bar")
        return self.search_input

    async def on_mount(self):
        self.title = "IntZam's MPV TUI"
        self.videos = [
            f for f in self.video_dir.iterdir() if f.is_file() and f.suffix.lower() in [".mp4", ".mkv", ".avi", ".mov"]
        ]
        self.filtered_videos = self.videos
        self.update_video_list()

    async def on_input_changed(self, event: Input.Changed):
        if event.input.id == "search-bar":
            query = event.value.lower().strip()
            self.filtered_videos = [video for video in self.videos if query in video.name.lower()]
            self.update_video_list()

    async def on_button_pressed(self, event: Button.Pressed):
        video_path = Path(event.button.name)
        if video_path.exists():
            self.selected_video = video_path  
            self.log(f"Selected video: {video_path.name}")
        else:
            self.log(f"Video path not found: {video_path}")

    def play_video(self, video_path: str):
        try:
            subprocess.run(["mpv", "--quiet", "--no-terminal", "--log-file=/dev/null", "--ao=pulse", video_path], check=True)
        except FileNotFoundError:
            self.log("MPV player not found. Make sure it is installed and in your PATH.")
        except subprocess.CalledProcessError as e:
            self.log(f"Failed to play video: {e}")

    async def on_key(self, event):
        if event.key == "r" and self.selected_video:
            
            self.log(f"Renaming {self.selected_video.name}. Type new name:")
            self.rename_input = Input(value=self.selected_video.stem, placeholder="Enter new name...")
            await self.mount(self.rename_input)  
            self.is_renaming = True  

        elif event.key == "enter":
            if self.is_renaming and self.rename_input:
                
                new_name = self.rename_input.value.strip()
                if new_name:
                    self.rename_video(self.selected_video, new_name)
                    self.log(f"Renamed video to {new_name}")
                await self.rename_input.remove()
                self.rename_input = None
                self.is_renaming = False
            elif self.selected_video:
                
                self.play_video(str(self.selected_video))

    def rename_video(self, old_path: Path, new_name: str):
        new_path = old_path.parent / f"{new_name}{old_path.suffix}"
        try:
            os.rename(old_path, new_path)
            
            self.videos = [
                f for f in self.video_dir.iterdir() if f.is_file() and f.suffix.lower() in [".mp4", ".mkv", ".avi", ".mov"]
            ]
            self.filtered_videos = self.videos
            self.update_video_list()
        except Exception as e:
            self.log(f"Error renaming video: {e}")

    def update_video_list(self):

        self.video_list.clear()
        for video in self.filtered_videos:
            safe_id = video.name.replace(" ", "_").replace("/", "_").replace("\\", "_").replace(":", "_")
            safe_id = ''.join([c if c.isalnum() or c in ['_', '-'] else '_' for c in safe_id])
            button = Button(video.name, id=safe_id, name=str(video))
            button.styles.hover_background = "blue"
            self.video_list.append(ListItem(button))


if __name__ == "__main__":
    VideoManagerApp().run()

