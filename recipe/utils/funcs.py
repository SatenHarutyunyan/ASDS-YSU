
def map_labels_to_classes(labels, classes):
    out = {}.fromkeys(set([i for i in labels]), [])
    indices_0 = [i for i, x in enumerate(labels) if x == 0]
    indices_1 = [i for i, x in enumerate(labels) if x == 1]
    indices_2 = [i for i, x in enumerate(labels) if x == 2]

    out[0] = [classes[i] for i in indices_0]
    out[1] = [classes[i] for i in indices_1]
    out[2] = [classes[i] for i in indices_2]
    return out