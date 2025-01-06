import clang.cindex

class ClassInfo:
    def __init__(self, name, attributes, methods, bases, is_abstract, is_struct):
        self.name = name
        self.attributes = attributes
        self.methods = methods
        self.bases = bases
        self.is_abstract = is_abstract,
        self.is_struct = is_struct

classes = {}        # Словник для зберігання інформації про класи
relationships = []  # Список для зберігання взаємозв'язків між класами

def _extract_classes(cursor):
    for child in cursor.get_children():
        if child.kind == clang.cindex.CursorKind.CLASS_DECL or child.kind == clang.cindex.CursorKind.STRUCT_DECL:
            _process_class(child)
        _extract_classes(child)  # Рекурсивний виклик

def _process_class(cursor):
    class_name = cursor.spelling
    if class_name in classes:
        return  # Клас вже оброблений

    # Окремо обробляємо атрибути, методи та базові класи
    attributes = []
    methods = []
    bases = []
    is_abstract = False
    is_struct = cursor.kind == clang.cindex.CursorKind.STRUCT_DECL;

    # Перевірка на абстрактність (якщо є віртуальні методи, можна вважати клас абстрактним)
    for child in cursor.get_children():
        if child.kind == clang.cindex.CursorKind.FIELD_DECL:
            attributes.append(child.spelling)  # Атрибути класу
        elif child.kind == clang.cindex.CursorKind.CXX_METHOD:
            methods.append(child.spelling)  # Методи класу
        elif child.kind == clang.cindex.CursorKind.CXX_BASE_SPECIFIER:
            bases.append(child.spelling)  # Базові класи
        elif child.kind == clang.cindex.CursorKind.CXX_ACCESS_SPEC_DECL:
            if child.spelling == "abstract":
                is_abstract = True  # Визначення абстрактного класу

    # Створення екземпляра ClassInfo
    class_info = ClassInfo(
        name=class_name,
        attributes=attributes,
        methods=methods,
        bases=bases,
        is_abstract=is_abstract,
        is_struct=is_struct
    )
    classes[class_name] = class_info

# Парсинг C++ файлу
index = clang.cindex.Index.create()
tu = index.parse('example.cpp', args=['-std=c++17'])

# Отримання кореневого курсору і початок обробки класів
root_cursor = tu.cursor
_extract_classes(root_cursor)

# Виведення зібраної інформації
for class_name, class_info in classes.items():
    if class_info.is_struct:
        print(f"Struct: {class_info.name}")
    else:
        print(f"Class: {class_info.name}")
    print(f"  Attributes: {class_info.attributes}")
    print(f"  Methods: {class_info.methods}")
    print(f"  Bases: {class_info.bases}")
    print(f"  Is Abstract: {class_info.is_abstract}")
    print("---")
