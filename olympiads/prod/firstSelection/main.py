# def main():
#     n = int(input())
#     ctrl_input = [input().strip() for _ in range(n)]
    
#     m = int(input())
#     queries = [input().strip() for _ in range(m)]
    
#     res = solve(ctrl_input, queries)
    
#     for r in res:
#         print(r)

# def solve(ctrl_input, queries):
#     ctrls = {}
#     for c_input in ctrl_input:
#         parts = c_input.split(" ")
#         ctrl_name = parts[0]
#         method = parts[1]
#         result = " ".join(parts[2:])
        
#         if ctrl_name not in ctrls:
#             ctrls[ctrl_name] = {}
#         ctrls[ctrl_name][method] = result
    
#     res = []
#     for q in queries:
#         ctrl_name, method_call = q.split(" ", 1)
        
#         if ctrl_name not in ctrls:
#             res.append("Method Not Found")
#             continue
        
#         ctrl = ctrls[ctrl_name]
#         found = False
#         for method, result in ctrl.items():
#             if '(' in method and ')' in method:
#                 method_name = method.split('(')[0]
#                 if method_call.startswith(method_name):
#                     param = method_call[len(method_name)+1:-1]
#                     result_str = result.replace("{id}", param)
#                     res.append(result_str)
#                     found = True
#                     break
#             elif method_call == method:
#                 res.append(result)
#                 found = True
#                 break
        
#         if not found:
#             res.append("Method Not Found")
    
#     return res

# if __name__ == "__main__":
#     main()                    # task 32




# class Transaction:
#     def __init__(self, client_id, mcc_code):
#         self.client_id = client_id
#         self.mcc_code = mcc_code

# def solve(n, m, transactions):
#     mcc_dict = {}

#     for t in transactions:
#         cid = t.client_id
#         mcc = t.mcc_code

#         if mcc not in mcc_dict:
#             mcc_dict[mcc] = {}

#         if cid not in mcc_dict[mcc]:
#             mcc_dict[mcc][cid] = 0

#         mcc_dict[mcc][cid] += 1

#     result = []

#     for mcc in sorted(mcc_dict.keys()):
#         max_cid = None
#         max_count = -1

#         for cid, count in mcc_dict[mcc].items():
#             if count > max_count or (count == max_count and cid < max_cid):
#                 max_count = count
#                 max_cid = cid

#         result.append(Transaction(max_cid, mcc))
#     return result

# def main():
#     n, m = map(int, input().split())
#     transactions = []

#     for _ in range(m):
#         client_id, mcc_code = map(int, input().split())
#         transactions.append(Transaction(client_id, mcc_code))

#     result = solve(n, m, transactions)

#     for entry in result:
#         print(entry.mcc_code, entry.client_id)

# if __name__ == "__main__":
#     main()                #  34
