import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import modules.GoodDay as GD
import modules.calculator as calc
import config as cfg

class Eurydice:
    
    with open("token.txt", 'r') as file:
        __token = file.read().replace('\n', '')
    __vkApi = vk_api.VkApi(token = __token)
    
    
    def __init__(self, name):
        
        self.name = name
        self.give = self.__vkApi.get_api()
        self.longpoll = VkLongPoll(self.__vkApi)
    
    
    def answer(self, id, text):
        self.__vkApi.method('messages.send', {'user_id' : id, 
                                              'message' : text, 
                                              'random_id': 0
                                              })

    
    def listen(self):
        
        while True:
            
            GD.sayOnTime(self, cfg.config_night_time_set, cfg.config_morning_time_set)
             
            for event in self.longpoll.check():
                
                if event.type == VkEventType.MESSAGE_NEW:

                    if event.to_me:
                        message = event.text.lower()
                        id = event.user_id
                        
                        if message == self.name.lower() + ", калькулятор":
                            calc.calculator(self, id, message, VkEventType.MESSAGE_NEW)
                        
                        elif message == self.name.lower() + ", привет" and \
                        id == 550581505:
                            self.answer(id, "Здравствуйте, хозяин")
                        
                        elif message == self.name.lower() + ", привет":
                            self.answer(id, 'Привет, я бот!')
                            print(id)
                        
                        elif message == 'как дела?':
                            self.answer(id, 'Хорошо, а твои как?' )
                        
                        else:
                            self.answer(id, 'Я вас не понимаю! :(')
