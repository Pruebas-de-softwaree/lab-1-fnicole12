import time
class UserManager:
    def __init__(self):
        self.users = []  

    def add_user(self, user_id, name):
        self.users.append({"id": user_id, "name": name})

    def find_user(self, user_id):
        user = None
        for u in self.users:
            if u["id"] == user_id:
                user = u
        return user  

    def delete_user(self, user_id):
        for u in self.users:
            if u["id"] == user_id:
                self.users.remove(u)
                break  

    def get_all_names(self):
        return [u["id"] for u in self.users]

    def average_user_id(self):
        return sum([u["id"] for u in self.users]) / len(self.users)


if __name__ == "__main__":
    user_manager = UserManager()
    
    #RF1 agregar 500 usuarios
    for i in range(500):
        user_manager.add_user(i, f"Yo soy el usuario num: {i}")
        
    #RF1 checar duplicados
    user_manager.add_user(1, f"Yo soy el verdadero numero 1")

    #RF2 checar id inexistente
    print(user_manager.find_user(600))

    #RF2 checar id existente
    print(user_manager.find_user(5))

    #RF3 borrar usuario existente
    user_manager.delete_user(3)
    print(user_manager.find(3))
    print("end")