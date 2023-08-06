import numpy as np

# Content: Dim | Node per cell | Node per face | Face per cell.
mesh_type_param = {"square": [2, 4, 2, 4]}


class AbstractMesh:
    def __init__(self, type, node_num, face_num, cell_num, float_dtype):
        self.cell_num = cell_num
        self.dim = mesh_type_param[type][0]
        self.face_num = face_num
        self.face_per_cell = mesh_type_param[type][3]
        self.node_num = node_num
        self.node_per_cell = mesh_type_param[type][1]
        self.node_per_face = mesh_type_param[type][2]

        self.cells = np.zeros([self.cell_num, self.node_per_cell], dtype=np.int32)
        self.cell_cell = np.zeros([self.cell_num, self.face_per_cell], dtype=np.int32)
        self.cell_volume = np.zeros([self.cell_num], dtype=float_dtype)
        self.cell_face = np.zeros([self.cell_num, self.face_per_cell], dtype=np.int32)
        self.cell_coord = np.zeros([self.cell_num, self.dim], dtype=float_dtype)
        self.faces = np.zeros([self.face_num, 2], dtype=np.int32)
        self.face_cell = np.full([self.face_num, 2], fill_value=-1, dtype=np.int32)
        self.face_center = np.zeros([self.face_num, self.dim], dtype=float_dtype)
        self.face_length = np.zeros([self.face_num], dtype=float_dtype)
        self.face_mark = np.zeros([self.face_num], dtype=np.int32)
        self.face_type = np.zeros([self.face_num, 3], dtype=float_dtype)
        self.face_norm = np.zeros([self.face_num, self.dim], dtype=float_dtype)
        self.nodes = np.zeros([self.node_num, self.dim], dtype=float_dtype)

    def _cal_cell_cell(self):
        print("[Error] Undefine cal cell cell function.")
        exit(7)

    def _cal_cell_coord(self):
        print("[Error] Undefine cal cell coord function.")
        exit(7)

    def _cal_cell_face(self):
        print("[Error] Undefine cal cell face function.")
        exit(7)

    def _cal_cell_volume(self):
        print("[Error] Undefine cal cell volume function.")
        exit(7)

    def _cal_cells(self):
        print("[Error] Undefine cal cells function.")
        exit(7)

    def _cal_face_cell(self):
        print("[Error] Undefine cal face cell function.")
        exit(7)

    def _cal_face_center(self):
        print("[Error] Undefine cal face center function.")
        exit(7)

    def _cal_face_length(self):
        print("[Error] Undefine cal face length function.")
        exit(7)

    def _cal_face_mark(self):
        print("[Error] Undefine cal face mark function.")
        exit(7)

    def _cal_face_norm(self):
        print("[Error] Undefine cal face norm function.")
        exit(7)

    def _cal_faces(self):
        print("[Error] Undefine cal faces function.")
        exit(7)

    def _cal_nodes(self):
        print("[Error] Undefine cal nodes function.")
        exit(7)

    def _generate(self):
        self._cal_nodes()
        self._cal_faces()
        self._cal_cells()

        self._cal_cell_cell()
        self._cal_cell_face()
        self._cal_face_cell()

        self._cal_face_center()
        self._cal_face_length()
        self._cal_cell_coord()
        self._cal_cell_volume()
        self._cal_face_norm()

        self._cal_face_mark()

