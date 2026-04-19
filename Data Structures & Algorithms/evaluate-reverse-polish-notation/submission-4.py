class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for t in tokens:
            if t not in "+-*/":
                st.append(int(t))
            else:
                r = st.pop()
                l = st.pop()
                if t== "+":
                    st.append(l+r)
                elif t== "-":
                    st.append(l-r)
                elif t== "*":
                    st.append(l*r)
                elif t== "/":
                    st.append(int(l/r))
    
            
        return st[-1]