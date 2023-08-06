"""
Make a square mesh topology.
* Index rule.
    (0, H)-------------------(L, H)
      |                         |
      |                         |
      |                         |
      |                         |
      |                         |
    (0, 0)-------------------(L, 0)
"""
import math
import numpy as np
from .abstract_mesh import AbstractMesh
# todo: Check if there is unallocate boundary.


class SquareMesh(AbstractMesh):
    def __init__(self, size, segment_num, float_dtype=np.float64):
        node_num = (segment_num[0] + 1)*(segment_num[1] + 1)
        face_num = segment_num[0]*(segment_num[1] + 1) + segment_num[1]*(segment_num[0] + 1)
        cell_num = segment_num[0]*segment_num[1]
        AbstractMesh.__init__(self, "square", node_num, face_num, cell_num, float_dtype)

        self.segment_num = segment_num
        self.size = size

        self._generate()

    def set_dirichlet_boundary(self, boundary_mark, value):
        """
        Set dirichely condition for boundary.
        :param boundary: Boundary mark (Left(1) | Up(2) | Right(3) | Down(4)).
        :param value: Boundary value.
        :return:
        """
        # todo: type check.
        for i in range(self.face_num):
            if self.face_mark[i] == boundary_mark:
                self.face_type[i, 0] = 1
                self.face_type[i, 1] = value
                self.face_type[i, 2] = 0

    def set_dirichlet_cos_boundary(self, boundary_mark):
        # todo: [Corner condition] Cos boundary is horizontal.
        for i in range(self.face_num):
            if self.face_mark[i] in boundary_mark:
                self.face_type[i, 0] = 1
                self.face_type[i, 1] = math.cos(self.face_center[i, 0]*360/self.size[0]*math.pi/180)
                self.face_type[i, 2] = 0

    def set_periodic_boundary(self, boundary_mark_pair):
        """
        Set periodic condition for boundary.
        Param: Boundary type | Adjacent face | Adjacent cell.
        :param boundary_mark_pair: Boundary mark (Left(1) | Up(2) | Right(3) | Down(4)).
        :return:
        """
        for i in range(self.face_num):
            if self.face_mark[i] == boundary_mark_pair[0]:
                for j in range(self.face_num):
                    if self.face_mark[j] == boundary_mark_pair[1] and abs(self.face_center[j][1] - self.face_center[i][1])<1e-15:
                        self.face_type[i, 0] = 4
                        self.face_type[i, 1] = j
                        self.face_type[i, 2] = self.face_cell[j, 0]
                        self.face_type[j, 0] = 4
                        self.face_type[j, 1] = i
                        self.face_type[j, 2] = self.face_cell[i, 0]

    def _cal_cell_cell(self):
        index = 0
        for j in range(self.segment_num[1]):
            for i in range(self.segment_num[0]):
                self.cell_cell[index][0] = self.__cell_index(i, j+1)
                self.cell_cell[index][1] = self.__cell_index(i+1, j)
                self.cell_cell[index][2] = self.__cell_index(i, j-1)
                self.cell_cell[index][3] = self.__cell_index(i-1, j)
                index += 1

    def _cal_cell_coord(self):
        for i in range(self.cell_num):
            for j in range(self.node_per_cell):
                self.cell_coord[i] += self.nodes[self.cells[i][j]]
            self.cell_coord[i] /= self.node_per_cell

    def _cal_cell_face(self):
        search = np.zeros([self.node_num, self.node_num], dtype=np.int32)

        for i in range(self.face_num):
            if self.faces[i, 0] < self.faces[i, 1]:
                search[self.faces[i, 0], self.faces[i, 1]] = i
            else:
                search[self.faces[i, 1], self.faces[i, 0]] = i

        for i in range(self.cell_num):
            for j in range(self.face_per_cell):
                tmp = j + 1 if j < self.face_per_cell - 1 else 0
                if self.cells[i, j] < self.cells[i, tmp]:
                    self.cell_face[i, j] = search[self.cells[i, j], self.cells[i, tmp]]
                else:
                    self.cell_face[i, j] = search[self.cells[i, tmp], self.cells[i, j]]

    def _cal_cell_volume(self):
        for i in range(self.cell_num):
            vector_0 = self.nodes[self.cells[i][0]] - self.nodes[self.cells[i][1]]
            vector_1 = self.nodes[self.cells[i][0]] - self.nodes[self.cells[i][3]]
            self.cell_volume[i] = abs(np.cross(vector_0, vector_1))

    def _cal_cells(self):
        index = 0
        for j in range(self.segment_num[1]):
            for i in range(self.segment_num[0]):
                self.cells[index][0] = self.__node_index(i, j)
                self.cells[index][1] = self.__node_index(i, j + 1)
                self.cells[index][2] = self.__node_index(i + 1, j + 1)
                self.cells[index][3] = self.__node_index(i + 1, j)
                index += 1

    def _cal_face_cell(self):
        for i in range(self.cell_num):
            for j in range(self.face_per_cell):
                if self.face_cell[self.cell_face[i, j], 0] == -1:
                    self.face_cell[self.cell_face[i, j], 0] = i
                else:
                    self.face_cell[self.cell_face[i, j], 1] = i

    def _cal_face_center(self):
        for i in range(self.face_num):
            self.face_center[i] = (self.nodes[self.faces[i,0]] + self.nodes[self.faces[i,1]])/2

    def _cal_face_length(self):
        for i in range(self.face_num):
            self.face_length[i] = np.linalg.norm(self.nodes[self.faces[i,0]] - self.nodes[self.faces[i,1]])

    def _cal_face_mark(self):
        """
        Left(1) | Up(2) | Right(3) | Down(4)
        :return:
        """
        for j in range(self.segment_num[1] + 1):
            for i in range(self.segment_num[1]):
                index = self.__horizontal_face_index(i, j)
                if j == 0:
                    self.face_mark[index] = 4
                elif j == self.segment_num[1]:
                    self.face_mark[index] = 2
                else:
                    self.face_mark[index] = 0

        for i in range(self.segment_num[0] + 1):
            for j in range(self.segment_num[1]):
                index = self.__vertical_face_index(i, j)
                if i == 0:
                    self.face_mark[index] = 1
                elif i == self.segment_num[0]:
                    self.face_mark[index] = 3
                else:
                    self.face_mark[index] = 0

    def _cal_face_norm(self):
        for i in range(self.face_num):
            x0 = self.nodes[self.faces[i, 0]][0]
            y0 = self.nodes[self.faces[i, 0]][1]
            x1 = self.nodes[self.faces[i, 1]][0]
            y1 = self.nodes[self.faces[i, 1]][1]

            if abs(x0 - x1) < 1e-15:
                self.face_norm[i][0] = 1
            elif abs(y0 - y1) < 1e-15:
                self.face_norm[i][1] = 1
            else:
                tmp = (x0 - x1)/(y1 - y0)
                self.face_norm[i][0] = 1/(1 + tmp**2)**0.5
                self.face_norm[i][1] = tmp/(1 + tmp**2)**0.5
            vector = self.cell_coord[self.face_cell[i, 0]] - (self.nodes[self.faces[i, 0]] + self.nodes[self.faces[i, 1]])/2
            if np.dot(self.face_norm[i], vector) > 0:
                self.face_norm[i] *= -1

    def _cal_faces(self):
        index = 0
        for j in range(self.segment_num[1] + 1):
            for i in range(self.segment_num[0]):
                self.faces[index][0] = self.__node_index(i, j)
                self.faces[index][1] = self.__node_index(i + 1, j)
                index += 1

        for i in range(self.segment_num[0] + 1):
            for j in range(self.segment_num[1]):
                self.faces[index][0] = self.__node_index(i, j)
                self.faces[index][1] = self.__node_index(i, j + 1)
                index += 1

    def _cal_nodes(self):
        """
        Outer loop change row(j), inner loop change column(i).
        :return:
        """
        delta_x = self.size[0]/self.segment_num[0]
        delta_y = self.size[1]/self.segment_num[1]
        index = 0
        for j in range(self.segment_num[1] + 1):
            for i in range(self.segment_num[0] + 1):
                self.nodes[index][0] = delta_x*i
                self.nodes[index][1] = delta_y*j
                index += 1

    def __cell_index(self, i, j):
        return -1 if i<0 or i>=self.segment_num[0] or j<0 or j>=self.segment_num[1] else self.segment_num[0]*j + i

    def __node_index(self, i, j):
        return (self.segment_num[0] + 1)*j + i

    def __horizontal_face_index(self, i, j):
        return self.segment_num[0]*j + i

    def __vertical_face_index(self, i, j):
        return (self.segment_num[1] + 1)*self.segment_num[0] + i*self.segment_num[1] + j

