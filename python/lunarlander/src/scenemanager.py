from  observer import EventNames

class SceneManager:
	def __init__(self, titlescreen_scene, lander_scene):
		self._titlescreen_scene = titlescreen_scene
		self._lander_scene = lander_scene
		self.scene = titlescreen_scene
	def switch_to(self, scene_name):
		if (scene_name == EventNames.EVENT_SWITCH_SCENE_TITLESCREEN):
			self.scene = self._titlescreen_scene
		if (scene_name == EventNames.EVENT_SWITCH_SCENE_LANDER):
			self.scene = self._lander_scene