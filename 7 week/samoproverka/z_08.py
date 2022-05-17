def token_parser(s):
    result = []
        count = ''
        for x in s:
          x_new = x.strip()
          print(x_new)
          if x_new == '':
            continue
          if x_new.isdigit():
            count += x_new
            print(count)
          else:
            if count != '':
                result.append(count)
                count = ''
            result.append(x_new)
        if count != '':
          result.append(count)
        print(result)
        return result