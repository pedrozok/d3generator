from d3generator.Config import Config

class RadialConfig(Config):
	
    label = ''
    diameter = 150
    min_value = 0
    max_value = 100
    value = 0

    def __init__(self, chart_type, container_id, label, value):
        Config.__init__(self,chart_type, container_id)
        self.label = label
        self.value = value

