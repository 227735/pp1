class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume_level = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

    def set_channels(self, channels_list):
        self.channels = channels_list

    def show_channels(self):
        print("Channel list:")
        for i, channel in enumerate(self.channels, start=1):
            print(f"{i}. {channel}")

    def increase_volume(self):
        if 0 <= self.volume_level < 10:
            self.volume_level += 1

    def decrease_volume(self):
        if 0 < self.volume_level <= 10:
            self.volume_level -= 1

    def show_status(self):
        if self.is_on:
            if 1 <= self.channel_no <= len(self.channels):
                channel_name = self.channels[self.channel_no - 1]
                print(f"TV is on, channel {self.channel_no} ({channel_name}), volume level {self.volume_level}")
            else:
                print(f"TV is on, channel {self.channel_no}, volume level {self.volume_level}")
        else:
            print("TV is off")

my_tv = TV()

available_channels = ["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery", "CNN"]
my_tv.set_channels(available_channels)

my_tv.turn_on()
my_tv.show_channels()
my_tv.increase_volume()
my_tv.show_status()
my_tv.increase_volume()
my_tv.show_status()
my_tv.decrease_volume()
my_tv.show_status()
my_tv.turn_off()
my_tv.show_status()