class Solution:
    def braceExpansionII(self,expression:str)->list[str]:
        i=0
        def parse():
            nonlocal i
            result=set()
            current={""}
            while i<len(expression) and expression[i]!='}':
                if expression[i]=='{':
                    i+=1
                    part=parse()
                    i+=1
                elif expression[i]==',':
                    result.update(current)
                    current={""}
                    i+=1
                    continue
                else:
                    part={expression[i]}
                    i+=1
                current={a+b for a in current for b in part}
            result.update(current)
            return result
        return sorted(parse())