class Stats:
    def __init__(self, eg_settings):
        self.eg_settings = eg_settings
        self.high_score = 0
        self.active_game = False
        self.play_again_flag = 1
        self.reset_stat()

    def reset_stat(self):
        self.virus_left = self.eg_settings.virus_limit

        self.score = 0
        self.level = 1
