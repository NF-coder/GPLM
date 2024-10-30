class TreeAPI:
    '''
        Класс для операций над деревом, абстракция над контроллером СУБД
    '''
    def __init__(self, DBController: object) -> None:
        self.DBController = DBController()
    
    def search_element(self, element: tuple):
        return self.DBController.search(
            element
        )