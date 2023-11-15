class Mobile () :
    def __init__(self, company_name, storage, serial_num, name, dual_sim, support_4k):
        self.company_name = company_name
        self.storage = storage
        self.serial_num = serial_num
        self.name = name
        self.dual_sim = dual_sim
        self.support_4k = support_4k

    def call(self):
        print("Calling from ",self.name)

    def send_message(self):
        print("Sending a message from ",self.name)

    def play_media(self):
        print("playing media on ",self.name)

my_mobile = Mobile("Samsung", 256, 4245762519, "s23 ultra", True, True)
print("Mobile Name: {}".format(my_mobile.name))
print("Storage Capacity:{}".format(my_mobile.storage),"GB")
print("Serial Number:{}".format(my_mobile.serial_num))
print("Serial Number:{}".format(my_mobile.dual_sim))
print("Supports 4K: {}".format(my_mobile.support_4k))

my_mobile.call()
my_mobile.send_message()
my_mobile.play_media()