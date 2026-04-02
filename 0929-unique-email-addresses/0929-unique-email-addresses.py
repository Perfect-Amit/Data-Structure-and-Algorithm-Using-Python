class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        st = set()
        for e in emails:
            local, domain = e.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            local = local.replace('.', '')
            st.add(local + '@' + domain)
        return len(st)