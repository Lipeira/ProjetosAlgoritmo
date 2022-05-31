class AVLtree:
    def __init__(self, person):
        self.left = None
        self.right = None
        self.height = 1
        self.person = person


def search(root, person):
    if root is None:
        return None

    if root.person == person:
        return True

    elif root.person < person:
        return search(root.right, person)

    elif root.person > person:
        return search(root.left, person)

    return False


def inorder(root, minimum):
    if root is not None:
        if root == minimum:
            print(root.person, end='')

        else:
            inorder(root.left, minimum)
            print('', root.person, end='')
            inorder(root.right, minimum)


def insert(root, person):
    element = AVLtree(person)

    if root is None:
        root = element
        return root

    elif element.person > root.person:
        if root.right is None:
            root.right = element
        root.right = insert(root.right, person)

    elif element.person < root.person:
        if root.left is None:
            root.left = element
        root.left = insert(root.left, person)

    else:
        pass

    root.height = max(heighttree(root.right), heighttree(root.left)) + 1

    balancefactor = balanceroot(root)

    if balancefactor < -1 and person < root.left.person:
        return rightrotate(root)

    elif balancefactor < -1 and person > root.left.person:
        root.left = leftrotate(root.left)
        return rightrotate(root)

    elif balancefactor > 1 and person < root.right.person:
        root.right = rightrotate(root.right)
        return leftrotate(root)

    elif balancefactor > 1 and person > root.right.person:
        return leftrotate(root)

    else:
        pass

    return root


def getmin(root):
    while root.left is not None:
        root = root.left

    return root


def getmax(root):
    while root.right is not None:
        root = root.right

    return root


def heighttree(root):
    if root is None:
        return 0

    heightleft = heighttree(root.left)
    heightright = heighttree(root.right)

    if heightleft > heightright:
        return heightleft + 1

    return heightright + 1


def balanceroot(root):
    if root is None:
        return 0

    return heighttree(root.right) - heighttree(root.left)


def leftrotate(person):

    next0 = person.right
    next1 = next0.left

    next0.left = person
    person.right = next1

    person.height = max(heighttree(person.right), heighttree(person.left)) + 1
    next0.height = max(heighttree(next0.right), heighttree(next0.left)) + 1

    return next0


def rightrotate(person):

    next2 = person.left
    next3 = next2.right

    next2.right = person
    person.left = next3

    person.height = max(heighttree(person.right), heighttree(person.left)) + 1
    next2.height = max(heighttree(next2.right), heighttree(next2.left)) + 1

    return next2


def remove(root, person):
    element = AVLtree(person)

    if root is None:
        return root

    elif element.person > root.person:
        root.right = remove(root.right, person)

    elif element.person < root.person:
        root.left = remove(root.left, person)

    else:
        if root.left is None and root.right is None:
            return None

        elif root.right is None:
            return root.left

        elif root.left is None:
            return root.right

        else:
            rev2 = getmin(root.right)
            root.person = rev2.person
            root.right = remove(root.right, rev2.person)

    root.height = max(heighttree(root.right), heighttree(root.left)) + 1

    balancefactor = balanceroot(root)

    if balancefactor < -1 and balanceroot(root.left) <= 0:
        return rightrotate(root)

    elif balancefactor < -1 and balanceroot(root.left) > 0:
        root.left = leftrotate(root.left)
        return rightrotate(root)

    elif balancefactor > 1 and balanceroot(root.right) >= 0:
        return leftrotate(root)

    elif balancefactor > 1 and balanceroot(root.right) < 0:
        root.right = rightrotate(root.right)
        return leftrotate(root)

    else:
        pass

    return root


def emptytree(root):
    if root is None:
        return True

    elif root is not None:
        return False

    else:
        pass


def main():
    roottree = None
    loop = True
    while loop:

        commands = input()
        command = commands.split()

        if command[0] == 'INSERT':
            name = str(command[1])

            if search(roottree, name) is None:
                roottree = insert(roottree, name)
                print('{name} ADICIONADO'.format(name=name))

            elif search(roottree, name) is False:
                roottree = insert(roottree, name)
                print('{name} ADICIONADO'.format(name=name))

            else:
                print('{name} JA EXISTE'.format(name=name))

        elif command[0] == 'DELETE':
            name = str(command[1])

            if search(roottree, name) is True:
                roottree = remove(roottree, name)
                print('{name} DELETADO'.format(name=name))

            else:
                print('{name} NAO ENCONTRADO'.format(name=name))

        elif command[0] == 'MIN':
            if emptytree is True:
                print('ARVORE VAZIA')
            else:
                minimum = getmin(roottree)
                print('MENOR: {minimum}'.format(minimum=minimum.person))

        elif command[0] == 'MAX':
            if emptytree is True:
                print('ARVORE VAZIA')
            else:
                maximum = getmax(roottree)
                print('MAIOR: {maximum}'.format(maximum=maximum.person))

        elif command[0] == 'ALT':
            alt = heighttree(roottree)
            print('ALTURA: {alt}'.format(alt=alt))

        elif command[0] == 'END':
            loop = False
            minimumextra = getmin(roottree)
            inorder(roottree, minimumextra)
            print()


if __name__ == '__main__':
    main()