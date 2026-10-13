#def parse_event(line):
with open('C:/Users/user/cs-practice/lab05/events-small.log', 'r', encoding='utf-8') as f:
        
        for line in f:
            a = line.split(':', 1)
            print(a)
            print(line)
        
