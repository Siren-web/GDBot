def calculator(object, local_id, local_message, msgEvent):
        
        object.answer(local_id, 'Что нужно решить?')
        for event in object.longpoll.listen():
            if event.type == msgEvent:
                if event.to_me:
                    local_message = event.text.lower()
                    local_id = event.user_id

                    otvet = eval(local_message)

                    object.answer(local_id, str(otvet) )
                    break