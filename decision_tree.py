#coding=utf-8

from common.utils import add

# gini-index based tree partition algorithm to generate decision tree to
# classfy.


class node:
    def __init__(self, point_set, feature_set, son_list=[], parent=None, label=None):
        self.point_set = point_set
        self.feature_set = feature_set
        self.son_list = son_list
        self.parent = parent
        self.label = label
        self.loss = None

class decision_tree:
    def __init__(self, feature_vectors, labels, Loss_criterion=GINI_INDEX):
        self.f_v = feature_vectors
        self.labels = labels
        self.point_list = []

    def train(self):
        #TODO can we use the generator to represent the point_set and feature_set
        point_set = [i for i in range(len(labels))]
        feature_set = [i for i in range(len(feature_vectors[0]))]
        #TODO feature_values could be map (value, point_i)
        feature_values = []
        for j in range(len(feature_vectors[0])):
            feature_values.append(sorted([(feature_vectors[i][j], i) for i in point_set ], key=lambda x: x[0]))
        self._grow_tree(point_set, feature_set, parent=None)

    def _grow_tree(self, point_set, feature_set, parent):
        if len(feature_set) == 0:
            return
        # feature_values = [[feature Xi's value tuple for dataset], ...] value
        # tuple's format is (value, data_id)
        # best_split = (split_best_cost_for_now, feature, split_f_value_data_id)

        feature_values = []
        for j in range(len(feature_set)):
            feature_values.append(sorted([(self.feature_vectors[i][j],i) for i in point_set], key=lambda x: x[0]))
        best_split = (+1, 0, 0)
        r_label_cnt = {}
        l_label_cnt = {}
        for feature in feature_set:
            for x_tuple in feature:
                label = self.labels[x_tuple[1]]
                add(r_label_cnt[label],1)
            for split_j-1 in range(len(feature_set)-1):


    def partition_score(self, ):
        pass

    def loss(self):
        pass

    def should_stop(self, ):
