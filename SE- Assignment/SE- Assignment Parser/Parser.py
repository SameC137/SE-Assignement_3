from collection import defaultdict
class node:
    def __init__(self,name,indentLevel,insideLoop):
        self.name = name
        self.next = None
        self.insideLoop=None
        self.indentLevel=indentLevel
    def __repr__(self):
        return self.name
class modifier:
    def __init__(self,name,indentLevel)
        self.name = name
        self.true = None
        self.false=None
        self.indentLevel=indentLevel
class Parser:
    def __init__(self,filename):
        self.fileName=filename
        self.conditions=defaultdict(list)
        self.indentList=defaultdict(list)        
        self.file=open(filename,"r")
        self.controlFlowModifiers=["while","for","if","elif","else:"]
    def parse(self):
        for line in self.file.readline():
            indentLevel=self.getIndentLevel(line)
            line=line.strip()
            if line.startswith('def'):
                self.graph[indentLevel].append(node(line,"functon def",indentLevel,false))
            elif line:
                firstWord=line.split()[0]
                if firstWord in self.controlFlowModifiers:
                    if(firstWord =='if'):
                        ifCondition=modifier(line[2:],indentLevel)
                        if self.indentList[indentLevel]:
                            self.indentList[indentLevel].next=ifCondition
                        else:
                            parent=self.indentList[indentLevel-1][-1]
                            if type(parent) is modifier:
                                parent.true=condition      
                            else:
                                self.indentList[indentLevel].append(ifCondition)
                        self.conditions[indentLevel].append(ifCondition)
                    elif firstWord == 'elif':
                        previousCondition=self.condition[indentLevel][-1]
                        elifCondition=modifier(line[4:],indentLevel)
                        previousCondition.false=elifCondition
                        self.indentList[indentLevel].append(elifCondition)
                        self.conditions[indentLevel].append(elifCondition)
                    elif firstWord == 'else:':
                        previousCondition=self.conditions[indentLevel][-1]
                        elseCondition=modifier("else",indentLevel)
                        previousCondition.false=elseCondition
                    else: 
                        parent=self.indentList[indentLevel-1][-1]
                        statement=node(line,indentLevel,false)
                        if not self.indentList[indentLevel]:
                            if(type(parent) is modifier):
                                if parent.indentLevel<=indentLevel:
                                    parent.false=statement
                                    parent.true.next=statement
                                else:
                                    parent.true=statement
                        
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
