import json
import os
import shutil

from manim import Scene, ThreeDScene, config

from .defaults import FOLDER_PATH


class Slide(Scene):
    def __init__(self, *args, output_folder=FOLDER_PATH, **kwargs):
        super(Slide, self).__init__(*args, **kwargs)
        self.output_folder = output_folder
        self.slides = list()
        self.current_slide = 1
        self.current_animation = 0
        self.loop_start_animation = None
        self.pause_start_animation = 0

    def play(self, *args, **kwargs):
        super(Slide, self).play(*args, **kwargs)
        self.current_animation += 1

    def pause(self):
        self.slides.append(dict(
            type="slide",
            start_animation=self.pause_start_animation,
            end_animation=self.current_animation,
            number=self.current_slide
        ))
        self.current_slide += 1
        self.pause_start_animation = self.current_animation

    def start_loop(self):
        assert self.loop_start_animation is None, "You cannot nest loops"
        self.loop_start_animation = self.current_animation

    def end_loop(self):
        assert self.loop_start_animation is not None, "You have to start a loop before ending it"
        self.slides.append(dict(
            type="loop",
            start_animation=self.loop_start_animation,
            end_animation=self.current_animation,
            number=self.current_slide
        ))
        self.current_slide += 1
        self.loop_start_animation = None
        self.pause_start_animation = self.current_animation

    def render(self, *args, **kwargs):
        # We need to disable the caching limit since we rely on intermidiate files
        max_files_cached = config["max_files_cached"]
        config["max_files_cached"] = float("inf")

        super(Slide, self).render(*args, **kwargs)

        config["max_files_cached"] = max_files_cached

        if not os.path.exists(self.output_folder):
            os.mkdir(self.output_folder)

        files_folder = os.path.join(self.output_folder, "files")
        if not os.path.exists(files_folder):
            os.mkdir(files_folder)

        scene_name = type(self).__name__
        scene_files_folder = os.path.join(files_folder, scene_name)

        if os.path.exists(scene_files_folder):
            shutil.rmtree(scene_files_folder)

        if not os.path.exists(scene_files_folder):
            os.mkdir(scene_files_folder)

        files = list()
        for src_file in self.renderer.file_writer.partial_movie_files:
            dst_file = os.path.join(scene_files_folder, os.path.basename(src_file))
            shutil.copyfile(src_file, dst_file)
            files.append(dst_file)

        f = open(os.path.join(self.output_folder, "%s.json" % (scene_name, )), "w")
        json.dump(dict(
            slides=self.slides,
            files=files
        ), f)
        f.close()

class ThreeDSlide(ThreeDScene, Slide):
    pass
