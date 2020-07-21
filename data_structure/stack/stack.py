class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)




code = '''
 t.field('updateAssessment', {
      type: 'Assessment',
      nullable: true,
      args: {
        assessmentId: idArg({ required: true }),
        data: arg({ required: true, type: 'AssessmentEditInput' }),
      }}))

'''
    
def isOpeningBrace(s):
    try:
        ['(','{','['].index(s)
        return True
    except ValueError:
        return False

def isClosingBrace(s):
    try:
        [')','}',']'].index(s)
        return True
    except ValueError:
        return False


def bracketLinter(code):
    brackets = {')':'(','}':'{',']':'['}
    stack = Stack()
    arr = []
    for s in code:
        if(isOpeningBrace(s)):
            stack.push(s)

        elif(isClosingBrace(s)):
            try:
                if(brackets[s] == stack.peek()):
                    stack.pop()
            except IndexError:
                print(f'you have extra closing bracket: {s}')
                return 1
       
    if(stack.size() > 0):
        print(f'you are missing a closing bracket: {stack.peek()}')
        return 1
    print("you don't have linting error!")
    return 0

bracketLinter(code)


