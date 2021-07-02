tasks_voc = {
    "debug":
        {
            0: [0, 1, 5],   
        },
    "offline":
        {
            0: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        },
    "19-1":
        {
            0: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
            1: [20],
        },
    "19-1b":
        {
            0: [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            1: [5],
        },
    "15-5":
        {
            0: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
            1: [16, 17, 18, 19, 20]
        },
    "15-5s":
        {
            0: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
            1: [16],
            2: [17],
            3: [18],
            4: [19],
            5: [20]
        },
    "10-5-5":
        {
            0: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            1: [11, 12, 13, 14, 15],
            2: [16, 17, 18, 19, 20]
        }
}
tasks_ade = {
    "offline":
        {
            0: [x for x in range(151)]
        },
    "100-50":
        {
            0: [x for x in range(0, 101)],
            1: [x for x in range(101, 151)]
        },
    "100-50b":
        {0: [0, 1, 3, 5, 6, 8, 9, 10, 12, 13, 14, 18, 19, 21, 22, 23, 24, 25, 26, 27,
             28, 29, 31, 32, 33, 34, 36, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 49,
             53, 54, 55, 56, 57, 58, 60, 61, 62, 63, 69, 70, 71, 74, 75, 76, 77, 80,
             81, 82, 84, 86, 87, 90, 91, 93, 95, 96, 99, 100, 101, 103, 104, 105, 106,
             107, 109, 113, 116, 117, 119, 120, 121, 123, 125, 126, 128, 129, 130,
             131, 132, 133, 134, 135, 136, 140, 142, 143, 144, 147, 148, 149, 150],
         1: [2, 4, 7, 11, 15, 16, 17, 20, 30, 35, 37, 41, 50, 51, 52, 59, 64, 65, 66,
             67, 68, 72, 73, 78, 79, 83, 85, 88, 89, 92, 94, 97, 98, 102, 108, 110,
             111, 112, 114, 115, 118, 122, 124, 127, 137, 138, 139, 141, 145, 146]
         },
    "100-50c":
        {0: [0, 1, 5, 6, 8, 9, 10, 11, 12, 13, 14, 16, 17, 19, 20, 23, 24, 25, 26, 27,
             28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 40, 41, 43, 44, 45, 46, 48, 50,
             52, 54, 56, 57, 61, 63, 65, 66, 67, 68, 69, 70, 71, 74, 76, 77, 78, 79,
             81, 82, 83, 84, 85, 86, 87, 90, 94, 95, 96, 97, 98, 99, 102, 105, 106,
             109, 110, 111, 112, 114, 115, 118, 119, 120, 121, 123, 124, 126, 128,
             129, 132, 133, 134, 135, 136, 138, 139, 142, 143, 144, 146, 147, 149],
         1: [2, 3, 4, 7, 15, 18, 21, 22, 38, 39, 42, 47, 49, 51, 53, 55, 58, 59, 60,
             62, 64, 72, 73, 75, 80, 88, 89, 91, 92, 93, 100, 101, 103, 104, 107, 108,
             113, 116, 117, 122, 125, 127, 130, 131, 137, 140, 141, 145, 148, 150]},
    "100-10":
        {
            0: [x for x in range(0, 101)],
            1: [x for x in range(101, 111)],
            2: [x for x in range(111, 121)],
            3: [x for x in range(121, 131)],
            4: [x for x in range(131, 141)],
            5: [x for x in range(141, 151)]
        },
    "100-10b":
        {0: [0, 1, 3, 5, 6, 8, 9, 10, 12, 13, 14, 18, 19, 21, 22, 23, 24, 25,
             26, 27, 28, 29, 31, 32, 33, 34, 36, 38, 39, 40, 42, 43, 44, 45,
             46, 47, 48, 49, 53, 54, 55, 56, 57, 58, 60, 61, 62, 63, 69, 70, 71,
             74, 75, 76, 77, 80, 81, 82, 84, 86, 87, 90, 91, 93, 95, 96, 99, 100,
             101, 103, 104, 105, 106, 107, 109, 113, 116, 117, 119, 120, 121,
             123, 125, 126, 128, 129, 130, 131, 132, 133, 134, 135, 136, 140,
             142, 143, 144, 147, 148, 149, 150],
         1: [11, 16, 50, 64, 66, 73, 89, 92, 145, 146],
         2: [30, 37, 51, 52, 72, 85, 98, 114, 115, 138],
         3: [2, 35, 65, 97, 110, 111, 112, 118, 124, 141],
         4: [4, 7, 15, 41, 67, 78, 79, 88, 108, 139],
         5: [17, 20, 59, 68, 83, 94, 102, 122, 127, 137]},
    "100-10c":
        {0: [0, 1, 5, 6, 8, 9, 10, 11, 12, 13, 14, 16, 17, 19, 20, 23, 24, 25, 26,
             27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 40, 41, 43, 44, 45, 46,
             48, 50, 52, 54, 56, 57, 61, 63, 65, 66, 67, 68, 69, 70, 71, 74, 76,
             77, 78, 79, 81, 82, 83, 84, 85, 86, 87, 90, 94, 95, 96, 97, 98, 99,
             102, 105, 106, 109, 110, 111, 112, 114, 115, 118, 119, 120, 121, 123,
             124, 126, 128, 129, 132, 133, 134, 135, 136, 138, 139, 142, 143, 144,
             146, 147, 149],
         1: [3, 4, 7, 18, 39, 64, 73, 101, 113, 137],
         2: [47, 51, 55, 60, 62, 80, 116, 127, 140, 148],
         3: [22, 42, 49, 58, 59, 89, 91, 92, 108, 125],
         4: [2, 38, 53, 100, 104, 117, 130, 131, 141, 145],
         5: [15, 21, 72, 75, 88, 93, 103, 107, 122, 150]},
    "50":
        {
            0: [x for x in range( 0, 51)],
            1: [x for x in range(51, 101)],
            2: [x for x in range(101, 151)]
        },
    "50b":
        {0: [0, 1, 9, 14, 18, 22, 24, 25, 27, 28, 29, 32, 38, 42, 45, 46, 47, 48, 49, 54, 56, 58, 61, 62, 63, 69, 74,
             75, 76, 77, 81, 82, 84, 90, 93, 96, 100, 103, 104, 109, 117, 119, 121, 123, 128, 129, 130, 134, 135,
             136, 144],
         1: [3, 5, 6, 8, 10, 12, 13, 19, 21, 23, 26, 31, 33, 34, 36, 39, 40, 43, 44, 53, 55, 57, 60, 70, 71, 80, 86,
             87, 91, 95, 99, 101, 105, 106, 107, 113, 116, 120, 125, 126, 131, 132, 133, 140, 142, 143, 147, 148,
             149, 150],
         2: [2, 4, 7, 11, 15, 16, 17, 20, 30, 35, 37, 41, 50, 51, 52, 59, 64, 65, 66, 67, 68, 72, 73, 78, 79, 83,
             85, 88, 89, 92, 94, 97, 98, 102, 108, 110, 111, 112, 114, 115, 118, 122, 124, 127, 137, 138, 139, 141,
             145, 146]
         },
    "50c":
        {0: [0, 5, 10, 11, 12, 13, 16, 17, 19, 20, 23, 27, 28, 30, 31, 32, 33, 37, 43, 46, 52, 56, 57, 65, 66, 69, 70, 74,
             76, 77, 79, 82, 83, 86, 87, 105, 109, 110, 111, 119, 128, 129, 132, 133, 134, 138, 142, 143, 144, 146,
             147],
         1: [1, 6, 8, 9, 14, 24, 25, 26, 29, 34, 35, 36, 40, 41, 44, 45, 48, 50, 54, 61, 63, 67, 68, 71, 78, 81, 84, 85,
             90, 94, 95, 96, 97, 98, 99, 102, 106, 112, 114, 115, 118, 120, 121, 123, 124, 126, 135, 136, 139, 149],
         2: [2, 3, 4, 7, 15, 18, 21, 22, 38, 39, 42, 47, 49, 51, 53, 55, 58, 59, 60, 62, 64, 72, 73, 75, 80, 88, 89, 91,
             92, 93, 100, 101, 103, 104, 107, 108, 113, 116, 117, 122, 125, 127, 130, 131, 137, 140, 141, 145, 148,
             150]
         }
}


def get_task_list():
    return list(tasks_voc.keys()) + list(tasks_ade.keys())


def get_task_labels(dataset, name, step):
    if dataset == 'voc':
        task_dict = tasks_voc[name]
    elif dataset == 'ade':
        task_dict = tasks_ade[name]
    else:
        raise NotImplementedError
    assert step in task_dict.keys(), f"You should provide a valid step! [{step} is out of range]"

    labels = list(task_dict[step])
    labels_old = [label for s in range(step) for label in task_dict[s]]
    return labels, labels_old, f'data/{dataset}/{name}'


def get_per_task_classes(dataset, name, step):
    if dataset == 'voc':
        task_dict = tasks_voc[name]
    elif dataset == 'ade':
        task_dict = tasks_ade[name]
    else:
        raise NotImplementedError
    assert step in task_dict.keys(), f"You should provide a valid step! [{step} is out of range]"

    classes = [len(task_dict[s]) for s in range(step+1)]
    return classes


def get_num_steps(dataset, name):
    if dataset == 'voc':
        task_dict = tasks_voc[name]
    elif dataset == 'ade':
        task_dict = tasks_ade[name]
    else:
        raise NotImplementedError

    numClasses = len(task_dict.keys())
    return numClasses
