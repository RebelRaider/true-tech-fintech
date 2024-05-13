import unittest
from uuid import UUID
from utils.utils import nlevel, uuid_to_ltree, list_to_ltree
from sqlalchemy_utils import Ltree


class TestMyModule(unittest.TestCase):
    def test_nlevel(self):
        # Проверяем, что функция возвращает правильное количество уровней в пути Ltree
        self.assertEqual(nlevel(Ltree("1")), 1)
        self.assertEqual(nlevel(Ltree("1.2")), 2)
        self.assertEqual(nlevel(Ltree("1.2.3")), 3)

    def test_uuid_to_ltree(self):
        # Проверяем, что UUID правильно преобразуется в Ltree
        uuid_str = "123e4567-e89b-12d3-a456-426614174000"
        expected_ltree = Ltree("123e4567.e89b.12d3.a456.426614174000")
        self.assertEqual(uuid_to_ltree(UUID(uuid_str)), expected_ltree)

    def test_list_to_ltree(self):
        # Проверяем, что список строк правильно преобразуется в Ltree
        input_list = ["1", "2", "3"]
        expected_ltree = Ltree("1.2.3")
        self.assertEqual(list_to_ltree(input_list), expected_ltree)

        # Проверяем случай с одним элементом в списке
        single_item_list = ["single"]
        self.assertEqual(list_to_ltree(single_item_list), Ltree("single"))


if __name__ == "__main__":
    unittest.main()
