class EventNames:
	EVENT_SWITCH_SCENE_TITLESCREEN = "switch-scene-titlescreen"
	EVENT_SWITCH_SCENE_LANDER = "switch-scene-lander"
	#KEYCHANGE_UP = "keychange-up"
	#KEYCHANGE_LEFT = "keychange-left"
	#KEYCHANGE_RIGHT = "keychange-right"

class Observer:
	def __init__(self):
		self._listeners = []
	def add_listener(self, listener):
		self._listeners.append(listener)
	def remove_listener(self, listener):
		self._listeners.remove(listener)
	def trigger(self, event):
		for listener in self._listeners:
			listener.trigger(event)

class Listener:
	def __init__(self, trigger_callback):
		self.trigger_callback = trigger_callback
	def trigger(self, event):
		self.trigger_callback(event)