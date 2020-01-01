def get_min_platforms(arr,dep):
    arri =[]
    arri2 = []
    for i in arr:
        arri.append(int(i.replace(":","")))
        arri2.append(int(i.replace(":", "")))
    depi = []
    for i in dep:
        depi.append(int(i.replace(":","")))
    print(arri)
    print(depi)

    platform = 0
    j = 0
    while arri2 :
        platform+=1
        for k in range(len(arri)):
            if depi[k] > j:
                j =arri[k]
                del arri2[k]





if __name__ == "__main__":
    arr =['9:00', '9:40', '9:50', '11:00', '15:00', '18:00']
    dep = ['9:10', '12:00', '11:20', '11:30', '19:00', '20:00']
    get_min_platforms(arr,dep)