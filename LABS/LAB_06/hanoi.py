def tower_of_hanoi_recursive(n, source, target, auxiliary):
    if n == 1:
        print("Disk 1 moved from", source, "to", target)
        return
    tower_of_hanoi_recursive(n-1, source, auxiliary, target)
    print("Disk", n, "moved from", source, "to", target)
    tower_of_hanoi_recursive(n-1, auxiliary, target, source)


tower_of_hanoi_recursive(3, 'A', 'C', 'B')
