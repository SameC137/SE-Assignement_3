from collection import defaultdict
class node:
    def __init__(self, name,typeOfNode,indentLevel,insideLoop):
        self.name = name
        self.next = None
        self.insideLoop=None
        self.indentLevel=indentLevel
    def __repr__(self):
        return self.name
class nodeWithBranchs:
    def __init__(self,name,indentLevel)
        self.name = name
        self.true = None
        self.false=None
        self.indentLevel=indentLevel
class Parser:
    def __init__(self,filename):
        self.fileName=filename
        self.graph=defaultdict(list)
        self.file=open(filename,"r")
        self.controlFlowModifiers=["while","for","if","elif","else:"]
    def parse(self):
        for line in self.file.readline():
            indentLevel=self.getIndentLevel(line)
            line=line.strip()
            ifline.stattswith('def'):
                self.graph[indentLevel].append(node("function Definition "+line))
            elif line:
                firstWord=line.split()[0]
                if firstWord in self.controlFlowModifiers:
                    if(firstWord =='if'):
                        condition=nodeWithBranches(line,indentLevel)
                        if_condition = Serial("if true")
                        condition.true = if_condition
                            
                            if self.graph[indentLevel]:  # if there's some other statement before me, i'm his next
                                self.graph[indentLevel][-1].next = condition
                            else:
                                parent = self.graph[indentLevel - 4][-1]  # one indent up, the last node is the parent
                                
                                if type(parent) is nodeWithBranches:  # if this is a nested if
                                    if not parent.true:  # if true branch is not taken, take it
                                        parent.true = condition
                                    else:
                                        parent.false = condition
                                else:
                                    parent.next = condition

                            self.graph[indentLevel].append(condition)
                            self.graph[indentLevel].append(if_condition)
                        elif firstWord == 'elif':
                            last_condition = self.getLastCondition(self.graph[indentLevel])
                            else_condition = Serial("if false")
                            new_condition = Condition('cond ' + trimmed[4:])
                            if_condition = Serial("if true")

                            last_condition.false = else_condition
                            else_condition.next = new_condition
                            new_condition.true = if_condition

                            self.graph[indentLevel].append(else_condition)
                            self.graph[indentLevel].append(new_condition)
                            self.graph[indentLevel].append(if_condition)

                        elif firstWord == 'else:':
                            last_condition = self.getLastCondition(self.graph[indentLevel])
                            else_condition = Serial("if false")
                            last_condition.false = else_condition
                            self.graph[indent_level].append(else_condition)
                        elif firstWord=='while':
                            condition=nodeWithBranches(line,indentLevel)
                            loopCondition = Serial("loop condition true")
                            condition.true = loopCondition
                            
                            if self.graph[indentLevel]:  # if there's some other statement before me, i'm his next
                                self.graph[indentLevel][-1].next = condition
                            else:
                                parent = self.graph[indentLevel - 4][-1]  # one indent up, the last node is the parent
                                
                                if type(parent) is Condition:  # if this is a nested if
                                    if not parent.true:  # if true branch is not taken, take it
                                        parent.true = condition
                                    else:
                                        parent.false = condition
                                else:
                                    parent.next = condition

                            self.graph[indentLevel].append(condition)
                            self.graph[indentLevel].append(if_condition)

                    else:  # here, they are just statements
                        statement = node(line)
                        
                        if not self.graph[indentLevel]:  # if i'm the first in my indent level
                            parent = self.graph[indentLevel - 1][-1]
                            parent.next = statement
                        else:
                            predecessor = self.graph[indent_level][-1]
                            predecessor.next = statement

                        self.graph[indentLevel].append(statement)
    def getLastCondition(self, indent_lane):
        for i in reversed(range(len(indent_lane))):
            if type(indent_lane[i]) is Condition:
                return indent_lane[i]

    def getIndentLevel(self,line):
        indent_level = 0
        for char in line:
            if char != ' ':
                return indent_level
            indent_level += 1
        indent_level=indent_level%4
        return indent_level
    def output_paths(self, entry):
        paths = []
        conditions = []
        def traverse(entry, path):
            path += ' -> ' + str(entry)           
            
            next_ = entry.next
            if next_ is None:
                paths.append(path)
                return

            if type(next_) is Condition:
                path += ' -> ' + str(next_)
                traverse(next_.true, path)
                traverse(next_.false, path)            
            else:
                traverse(next_, path)
        
        traverse(entry, '')
        for path in paths:
            print(path)


