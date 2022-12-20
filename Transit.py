def pick_peaks(arr):
    arr1=arr
    print(arr1)
    peaks = []
    pos = []
    i=0
    if arr1[len(arr1)-1]>arr1[len(arr1)-2]:
        del arr1[len(arr1)-1]
    if arr1[i]>arr1[i+1]:
        i+=1
    if arr1.count(arr1[0])==len(arr1):
        return peaks, pos
    while i<(len(arr)-1):
        if arr1[i]<arr1[i+1]:
            i+=1
        elif arr1[i]>arr1[i+1]:
            if arr1[i] not in peaks:
                peaks.append(arr1[i])
                pos.append(arr1.index(arr1[i]))
                i+=1
            i+=1
        elif arr1[i]==arr1[i+1]:
            peaks.append(arr1[i])
            pos.append(arr1.index(arr1[i]))
            while arr1[i]==arr1[i+1]:
                # print(i)
                if i==len(arr)-2:
                    del peaks[len(peaks)-1]
                    del pos[len(pos) - 1]
                    return peaks, pos
                i+=1
            break
        else:
            continue
    if peaks[0]==arr1[0]:
        print(peaks[0], arr1[0])
        del peaks[0]
        del pos[0]
    return peaks, pos

if __name__ == '__main__':
    # pick_peaks([1,2,5,6,6,2,3,4,4,1,2])
    # pick_peaks([35,50, 50, 50, 50, 35])
    # pick_peaks([35,35,35,35,35,35,35])
    print(pick_peaks([17, 18, 10, -25, -4, 15, 15]))
    print(pick_peaks([35, 50, 50, 50, 50, 49]))
    print(pick_peaks([36,35,35,36,35,35,35]))