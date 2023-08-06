from os import name

import codecs
import os

#create html sessions object
web_session = requests.Session()

#fake user agent
user_agent = {"User-Agent" : "Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"}

def clear():
    if name == "nt":
        os.system("cls")

    else:
        os.system("clear")

#scans for hyperlinks using get requests
def link_scanner(url):
    #variables
    i = -1
    original_url = url
    output = https_string + url
    total_web_list = []
    total_web_list.append(output)
    result_list = []
    web_list = []

    clear()

    user_input = input("1 = search domain links | 2 = search all links | 3 = search for a specific link | 4 = search domain links using selenium\n")

    if user_input == "3":
        specific_link = input("enter specific link: ")

    if user_input == "4":
        return link_scanner_selenium(url)

    while True:
        try:
            total_web_list = list(dict.fromkeys(total_web_list))
            
            i += 1

            if termux_tor_boolean == True or tor_boolean == True:
                final = web_session.get(total_web_list[i], verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = (5, 30))

            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                final = web_session.get(total_web_list[i], verify = valid_certificate, headers = user_agent, timeout = (5, 30))
                
            found = str(final.status_code)

            if found == "200" and len(final.text) <= 1000000:
                try:
                    print(total_web_list[i])
                    result = str(final.text)

                    soup = BeautifulSoup(result, "html.parser")

                    for my_link in soup.find_all("a", href = True):
                        if "http://" in my_link["href"] or "https://" in my_link["href"]:
                            web_list.append(my_link["href"])

                        if "http://" not in my_link["href"] and "https://" not in my_link["href"]:
                            try:
                                if my_link["href"].index("/") == 0:
                                    web_list.append(str(output + my_link["href"]))

                            except:
                                web_list.append(str(output + "/" + my_link["href"]))
                                
                    web_list = list(dict.fromkeys(web_list))
                    web_list.sort()

                except:
                    print("ERROR!")

                for j in web_list:
                    
                    if user_input == "1":
                        domain_name = str(original_url) in j

                        if domain_name == True:
                            parse = re.findall(r'(?<=<a href="/)[^"]*', result)
                            parse = list(dict.fromkeys(parse))
                            parse.sort()

                            for href in parse:
                                href_result = output + href
                                total_web_list.append(href_result)
                            
                            if "\'" in j:
                                j.split("\'")
                                total_web_list.append(j[0])

                            if "<" in j:
                                j.split("<")
                                total_web_list.append(j[0])

                            if "\\" in j:
                                j.split("\\")
                                total_web_list.append(j[0])

                            if "href" in j:
                                j.split("href")
                                total_web_list.append(j[0])

                            if ")" in j:
                                j.split(")")
                                total_web_list.append(j[0])

                            else:
                                total_web_list.append(j)
                            
                    if user_input == "2":
                        if "\'" in j:
                            j.split("\'")
                            total_web_list.append(j[0])

                        if "<" in j:
                            j.split("<")
                            total_web_list.append(j[0])

                        if "\\" in j:
                            j.split("\\")
                            total_web_list.append(j[0])

                        if "href" in j:
                            j.split("href")
                            total_web_list.append(j[0])

                        if ")" in j:
                                j.split(")")
                                total_web_list.append(j[0])

                        else:
                            total_web_list.append(j)

                    if user_input == "3":
                        domain_name = str(original_url) in j

                        if domain_name == True:
                            if "\'" in j:
                                j.split("\'")
                                total_web_list.append(j[0])

                            if "<" in j:
                                j.split("<")
                                total_web_list.append(j[0])

                            if "\\" in j:
                                j.split("\\")
                                total_web_list.append(j[0])

                            if "href" in j:
                                j.split("href")
                                total_web_list.append(j[0])

                            if ")" in j:
                                j.split(")")
                                total_web_list.append(j[0])

                            else:
                                total_web_list.append(j)

                            for k in web_list:
                                specific = str(specific_link) in k

                                if specific == True:
                                    if "\'" in k:
                                        k.split("\'")
                                        result_list.append(k[0])

                                    if "<" in k:
                                        k.split("<")
                                        result_list.append(k[0])

                                    if "\\" in k:
                                        k.split("\\")
                                        result_list.append(k[0])

                                    if "href" in k:
                                        k.split("href")
                                        total_web_list.append(k[0])

                                    if ")" in k:
                                        k.split(")")
                                        total_web_list.append(k[0])

                                    else:
                                        result_list.append(k)

            else:
                continue
                    
        except requests.exceptions.SSLError:
            print("ERROR: invalid certificate!")
            continue

        except requests.exceptions.ChunkedEncodingError:
            print("ERROR: chunked encoding error!")
            continue

        except urllib3.exceptions.LocationParseError:
            print("ERROR: location parse error!")
            continue

        except requests.exceptions.ConnectionError:
            print("ERROR: connection error!")
            continue

        except requests.exceptions.ConnectTimeout:
            print("ERROR: connect timeout!")
            continue

        except requests.exceptions.InvalidSchema:
            print("ERROR: invalid schema!")
            continue

        except requests.exceptions.InvalidURL:
            print("ERROR: invalid url!")
            continue

        except requests.exceptions.MissingSchema:
            print("ERROR: missing schema!")
            continue

        except requests.exceptions.TooManyRedirects:
            print("ERROR: too many redirects!")
            continue

        except requests.exceptions.ReadTimeout:
            print("ERROR: read timeout!")
            continue
            
        except IndexError:
            break

    clear()
    result_list = list(dict.fromkeys(result_list))
    total_web_list = list(dict.fromkeys(total_web_list))
    
    result_list.sort()

    if user_input == "1" or user_input == "2":
        return total_web_list

    if user_input == "3":
        return result_list

#scans for hyperlinks using selenium
def link_scanner_selenium(url):
    result = https_string + url
    
    driver = webdriver.Firefox(service = Service(GeckoDriverManager().install()))
    clear()

    i = -1
    total_web_list = []
    total_web_list.append(result)
    web_list = []

    while True:
        i = i + 1
        
        try:
            print(total_web_list[i])
            driver.get(total_web_list[i])

        except IndexError:
            break

        except:
            continue
        
        try:
            for ii in driver.find_elements(by = By.XPATH, value = ".//a"):
                web_list.append(ii.get_attribute("href"))

        except:
            pass

        web_list = list(dict.fromkeys(web_list))

        for iii in web_list:
            try:
                domain_name = result in iii

                parse = iii.index(result, 0, len(result))
                
                if domain_name == True and parse == 0:
                    total_web_list.append(iii)
                    total_web_list = list(dict.fromkeys(total_web_list))

            except:
                continue

    total_web_list = list(dict.fromkeys(total_web_list))
    total_web_list.sort()

    clear()

    return total_web_list

def source_code_viewer(file, keyword):
    clear()

    my_boolean = False

    count = 0
    
    with open(file, "rb") as f:
        for chunk in iter(lambda: f.read(128), b""):
            try:
                ascii_convert = codecs.decode(chunk, "ascii")
            
                clean = str(ascii_convert).replace("b", "")
                clean = clean.replace("'", "")
                clean = clean.replace("\x00", "")
                clean = clean.replace("\x11", "")

                my_list = list(clean)
                my_list = list(set(my_list))

                if len(my_list) != 1 and my_list[0] != "\\x00" and keyword in clean:
                    print(clean)

                    count += 1

                    if count == 64:
                        count = 0
                        pause = input()
                    
            except:
                pass

    print("\ndone")

def sql_injection_scanner(url):
    clear()
    my_url = https_string + url

    #sql errors
    error_mesage = {"SQL syntax.*?MySQL", "Warning.*?\Wmysqli?_", "MySQLSyntaxErrorException", "valid MySQL result", "check the manual that (corresponds to|fits) your MySQL server version", "check the manual that (corresponds to|fits) your MariaDB server version", "check the manual that (corresponds to|fits) your Drizzle server version", "Unknown column '[^ ]+' in 'field list'", "MySqlClient\.", "com\.mysql\.jdbc", "Zend_Db_(Adapter|Statement)_Mysqli_Exception", "Pdo\[./_\\]Mysql", "MySqlException", "SQLSTATE\[\d+\]: Syntax error or access violation", "MemSQL does not support this type of query", "is not supported by MemSQL", "unsupported nested scalar subselect", "PostgreSQL.*?ERROR", "Warning.*?\Wpg_", "valid PostgreSQL result", "Npgsql\.", "PG::SyntaxError:", "org\.postgresql\.util\.PSQLException", "ERROR:\s\ssyntax error at or near", "ERROR: parser: parse error at or near", "PostgreSQL query failed", "org\.postgresql\.jdbc", "Pdo\[./_\\]Pgsql", "PSQLException", "OLE DB.*? SQL Server", "\bSQL Server[^&lt;&quot;]+Driver", "Warning.*?\W(mssql|sqlsrv)_", "\bSQL Server[^&lt;&quot;]+[0-9a-fA-F]{8}", "System\.Data\.SqlClient\.(SqlException|SqlConnection\.OnError)", "(?s)Exception.*?\bRoadhouse\.Cms\.", "Microsoft SQL Native Client error '[0-9a-fA-F]{8}", "\[SQL Server\]", "ODBC SQL Server Driver", "ODBC Driver \d+ for SQL Server", "SQLServer JDBC Driver", "com\.jnetdirect\.jsql", "macromedia\.jdbc\.sqlserver", "Zend_Db_(Adapter|Statement)_Sqlsrv_Exception", "com\.microsoft\.sqlserver\.jdbc", "Pdo\[./_\\](Mssql|SqlSrv)", "SQL(Srv|Server)Exception", "Unclosed quotation mark after the character string", "Microsoft Access (\d+ )?Driver", "JET Database Engine", "Access Database Engine", "ODBC Microsoft Access", "Syntax error \(missing operator\) in query expression", "\bORA-\d{5}", "Oracle error", "Oracle.*?Driver", "Warning.*?\W(oci|ora)_", "quoted string not properly terminated", "SQL command not properly ended", "macromedia\.jdbc\.oracle", "oracle\.jdbc", "Zend_Db_(Adapter|Statement)_Oracle_Exception", "Pdo\[./_\\](Oracle|OCI)", "OracleException", "CLI Driver.*?DB2", "DB2 SQL error", "\bdb2_\w+\(", "SQLCODE[=:\d, -]+SQLSTATE", "com\.ibm\.db2\.jcc", "Zend_Db_(Adapter|Statement)_Db2_Exception", "Pdo\[./_\\]Ibm", "DB2Exception", "ibm_db_dbi\.ProgrammingError", "Warning.*?\Wifx_", "Exception.*?Informix", "Informix ODBC Driver", "ODBC Informix driver", "com\.informix\.jdbc", "weblogic\.jdbc\.informix", "Pdo\[./_\\]Informix", "IfxException", "Dynamic SQL Error", "Warning.*?\Wibase_", "org\.firebirdsql\.jdbc", "Pdo\[./_\\]Firebird", "SQLite/JDBCDriver", "SQLite\.Exception", "(Microsoft|System)\.Data\.SQLite\.SQLiteException", "Warning.*?\W(sqlite_|SQLite3::)", "\[SQLITE_ERROR\]", "SQLite error \d+:", "sqlite3.OperationalError:", "SQLite3::SQLException", "org\.sqlite\.JDBC", "Pdo\[./_\\]Sqlite", "SQLiteException", "SQL error.*?POS([0-9]+)", "Warning.*?\Wmaxdb_", "DriverSapDB", "-3014.*?Invalid end of SQL statement", "com\.sap\.dbtech\.jdbc", "\[-3008\].*?: Invalid keyword or missing delimiter", "Warning.*?\Wsybase_", "Sybase message", "Sybase.*?Server message", "SybSQLException", "Sybase\.Data\.AseClient", "com\.sybase\.jdbc", "Warning.*?\Wingres_", "Ingres SQLSTATE", "Ingres\W.*?Driver", "com\.ingres\.gcf\.jdbc", "Exception (condition )?\d+\. Transaction rollback", "com\.frontbase\.jdbc", "Syntax error 1. Missing", "(Semantic|Syntax) error [1-4]\d{2}\.", "Unexpected end of command in statement \[", "Unexpected token.*?in statement \[", "org\.hsqldb\.jdbc", "org\.h2\.jdbc", "\[42000-192\]", "![0-9]{5}![^\n]+(failed|unexpected|error|syntax|expected|violation|exception)", "\[MonetDB\]\[ODBC Driver", "nl\.cwi\.monetdb\.jdbc", "Syntax error: Encountered", "org\.apache\.derby", "ERROR 42X01", ", Sqlstate: (3F|42).{3}, (Routine|Hint|Position):", "/vertica/Parser/scan", "com\.vertica\.jdbc", "org\.jkiss\.dbeaver\.ext\.vertica", "com\.vertica\.dsi\.dataengine", "com\.mckoi\.JDBCDriver", "com\.mckoi\.database\.jdbc", "&lt;REGEX_LITERAL&gt;", "com\.facebook\.presto\.jdbc", "io\.prestosql\.jdbc", "com\.simba\.presto\.jdbc", "UNION query has different number of fields: \d+, \d+", "Altibase\.jdbc\.driver", "com\.mimer\.jdbc", "Syntax error,[^\n]+assumed to mean", "io\.crate\.client\.jdbc", "encountered after end of query", "A comparison operator is required here", "-10048: Syntax error", "rdmStmtPrepare\(.+?\) returned", "SQ074: Line \d+:", "SR185: Undefined procedure", "SQ200: No table ", "Virtuoso S0002 Error", "\[(Virtuoso Driver|Virtuoso iODBC Driver)\]\[Virtuoso Server\]"}
    
    #malicious sql code
    mal_sql = ["\"", "\'", ";"]

    my_list = []

    user_input = input("1 = scan url | 2 = scan url and hyperlinks\n")
    clear()
    
    if user_input == "1":
        for c in mal_sql:
            new_url = f"{my_url}{c}"
            print("checking: " + new_url)
            
            try:
                result = web_session.get(new_url, verify = True, headers = user_agent, timeout = (5, 30))

                for i in error_mesage:
                    my_regex = re.search(i, result.text)
                    my_boolean = False

                    try:
                        if my_regex:
                            my_boolean = True
                            break

                    except UnicodeDecodeError:
                        break

                if my_boolean == True:
                    print("true: " + new_url)
                    my_list.append(new_url)

            except requests.exceptions.SSLError:
                print("ERROR: invalid certificate!")
                continue

            except urllib3.exceptions.LocationParseError:
                print("ERROR: location parse error!")
                continue

            except requests.exceptions.ConnectionError:
                print("ERROR: connection error!")
                continue

            except requests.exceptions.ConnectTimeout:
                print("ERROR: connect timeout!")
                continue

            except requests.exceptions.InvalidSchema:
                print("ERROR: invalid schema!")
                continue

            except requests.exceptions.InvalidURL:
                print("ERROR: invalid url!")
                continue

            except requests.exceptions.MissingSchema:
                print("ERROR: missing schema!")
                continue

            except requests.exceptions.TooManyRedirects:
                print("ERROR: too many redirects!")
                continue

            except requests.exceptions.ReadTimeout:
                print("ERROR: read timeout!")
                continue

        try:
            print("checking for forms on: " + my_url)
            
            if termux_tor_boolean == True or tor_boolean == True:
                result = web_session.get(my_url, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = (5, 30))

            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                result = web_session.get(my_url, verify = valid_certificate, headers = user_agent, timeout = (5, 30))

            try:
                soup = BeautifulSoup(result.text, "html.parser")
                get_input = soup.find_all("input")

            except:
                pass

            form_list = []

            for i in get_input:
                if "email" in str(i):
                    form_name = ""

                    try:
                        parse_name_start = str(i).index("name=\"")
                        parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                        for ii in range(parse_name_start + 6, parse_name_end):
                            form_name = form_name + str(i)[ii]

                        form_list.append(form_name)

                    except:
                        pass

                if "hidden" in str(i):
                    form_name = ""

                    try:
                        parse_name_start = str(i).index("name=\"")
                        parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                        for ii in range(parse_name_start + 6, parse_name_end):
                            form_name = form_name + str(i)[ii]

                        form_list.append(form_name)

                    except:
                        pass
                    
                if "number" in str(i):
                    form_name = ""

                    try:
                        parse_name_start = str(i).index("name=\"")
                        parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                        for ii in range(parse_name_start + 6, parse_name_end):
                            form_name = form_name + str(i)[ii]

                        form_list.append(form_name)

                    except:
                        pass

                if "password" in str(i):
                    form_name = ""

                    try:
                        parse_name_start = str(i).index("name=\"")
                        parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                        for ii in range(parse_name_start + 6, parse_name_end):
                            form_name = form_name + str(i)[ii]

                        form_list.append(form_name)

                    except:
                        pass

                if "query" in str(i):
                    form_name = ""

                    try:
                        parse_name_start = str(i).index("name=\"")
                        parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                        for ii in range(parse_name_start + 6, parse_name_end):
                            form_name = form_name + str(i)[ii]

                        form_list.append(form_name)

                    except:
                        pass

                if "search" in str(i):
                    form_name = ""

                    try:
                        parse_name_start = str(i).index("name=\"")
                        parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))
                        
                        for ii in range(parse_name_start + 6, parse_name_end):
                            form_name = form_name + str(i)[ii]

                        form_list.append(form_name)

                    except:
                        pass

                if "tel" in str(i):
                    form_name = ""

                    try:
                        parse_name_start = str(i).index("name=\"")
                        parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                        for ii in range(parse_name_start + 6, parse_name_end):
                            form_name = form_name + str(i)[ii]

                        form_list.append(form_name)

                    except:
                        pass

                if "text" in str(i):
                    form_name = ""

                    try:
                        parse_name_start = str(i).index("name=\"")
                        parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                        for ii in range(parse_name_start + 6, parse_name_end):
                            form_name = form_name + str(i)[ii]

                        form_list.append(form_name)

                    except:
                        pass

                if "url" in str(i):
                    form_name = ""

                    try:
                        parse_name_start = str(i).index("name=\"")
                        parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                        for ii in range(parse_name_start + 6, parse_name_end):
                            form_name = form_name + str(i)[ii]

                        form_list.append(form_name)

                    except:
                        pass

            form_list = list(dict.fromkeys(form_list))
            form_list.sort()

            for forms in form_list:
                for mal in mal_sql:
                    form_dict = {forms: mal}

                    print("checking form (" + mal + "): " + forms)

                    if termux_tor_boolean == True or tor_boolean == True:
                        send_data = web_session.post(my_url, data = form_dict, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = (5, 30))

                    if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                        send_data = web_session.post(my_url, data = form_dict, verify = valid_certificate, headers = user_agent, timeout = (5, 30))

                    for i in error_mesage:
                        my_regex = re.search(i, send_data.text)
                        my_boolean = False

                        try:
                            if my_regex:
                                    my_boolean = True
                                    break

                        except UnicodeDecodeError:
                            continue

                    if my_boolean == True:
                        print("true: " + url + " form: " + forms)
                        my_list.append(url + " form: " + forms)

                    if termux_tor_boolean == True or tor_boolean == True:
                        get_data = web_session.get(my_url, params = form_dict, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = (5, 30))

                    if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                        get_data = web_session.get(my_url, params = form_dict, verify = valid_certificate, headers = user_agent, timeout = (5, 30))

                    for i in error_mesage:
                        my_regex = re.search(i, get_data.text)
                        my_boolean = False

                        try:
                            if my_regex:
                                    my_boolean = True
                                    break

                        except UnicodeDecodeError:
                            continue

                    if my_boolean == True:
                        print("true: " + url + " form: " + forms)
                        my_list.append(url + " form: " + forms)

        except requests.exceptions.SSLError:
            print("ERROR: invalid certificate!")
            pass

        except urllib3.exceptions.LocationParseError:
            print("ERROR: location parse error!")
            pass

        except requests.exceptions.ConnectionError:
            print("ERROR: connection error!")
            pass

        except requests.exceptions.ConnectTimeout:
            print("ERROR: connect timeout!")
            pass

        except requests.exceptions.InvalidSchema:
            print("ERROR: invalid schema!")
            pass

        except requests.exceptions.InvalidURL:
            print("ERROR: invalid url!")
            pass

        except requests.exceptions.MissingSchema:
            print("ERROR: missing schema!")
            pass

        except requests.exceptions.TooManyRedirects:
            print("ERROR: too many redirects!")
            pass

        except requests.exceptions.ReadTimeout:
            print("ERROR: read timeout!")
            pass

    if user_input == "2":
        my_result = link_scanner(url)

        for j in my_result:
            for c in mal_sql:
                new_url = f"{j}{c}"

                print("checking: " + new_url)

                try:
                    if termux_tor_boolean == True or tor_boolean == True:
                        result = web_session.get(new_url, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = (5, 30))

                    if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                        result = web_session.get(new_url, verify = valid_certificate, headers = user_agent, timeout = (5, 30))

                    for i in error_mesage:
                        my_regex = re.search(i, result.text)
                        my_boolean = False

                        try:
                            if my_regex:
                                my_boolean = True
                                break

                        except UnicodeDecodeError:
                            continue

                    if my_boolean == True:
                        print("true: " + new_url)
                        my_list.append(new_url)

                except requests.exceptions.SSLError:
                    print("ERROR: invalid certificate!")
                    pass

                except urllib3.exceptions.LocationParseError:
                    print("ERROR: location parse error!")
                    pass

                except requests.exceptions.ConnectionError:
                    print("ERROR: connection error!")
                    pass

                except requests.exceptions.ConnectTimeout:
                    print("ERROR: connect timeout!")
                    pass

                except requests.exceptions.InvalidSchema:
                    print("ERROR: invalid schema!")
                    pass

                except requests.exceptions.InvalidURL:
                    print("ERROR: invalid url!")
                    pass

                except requests.exceptions.MissingSchema:
                    print("ERROR: missing schema!")
                    pass

                except requests.exceptions.TooManyRedirects:
                    print("ERROR: too many redirects!")
                    pass

                except requests.exceptions.ReadTimeout:
                    print("ERROR: read timeout!")
                    pass
                
            try:
                print("checking for forms on: " + j)

                if termux_tor_boolean == True or tor_boolean == True:
                    result = web_session.get(j, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = (5, 30))

                if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                    result = web_session.get(j, verify = valid_certificate, headers = user_agent, timeout = (5, 30))

                try:
                    soup = BeautifulSoup(result.text, "html.parser")
                    get_input = soup.find_all("input")

                except:
                    pass

                form_list = []

                for i in get_input:
                    if "email" in str(i):
                        form_name = ""

                        try:
                            parse_name_start = str(i).index("name=\"")
                            parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                            for ii in range(parse_name_start + 6, parse_name_end):
                                form_name = form_name + str(i)[ii]

                            form_list.append(form_name)

                        except:
                            pass

                    if "hidden" in str(i):
                        form_name = ""

                        try:
                            parse_name_start = str(i).index("name=\"")
                            parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                            for ii in range(parse_name_start + 6, parse_name_end):
                                form_name = form_name + str(i)[ii]

                            form_list.append(form_name)

                        except:
                            pass
                        
                    if "number" in str(i):
                        form_name = ""

                        try:
                            parse_name_start = str(i).index("name=\"")
                            parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                            for ii in range(parse_name_start + 6, parse_name_end):
                                form_name = form_name + str(i)[ii]

                            form_list.append(form_name)

                        except:
                            pass

                    if "password" in str(i):
                        form_name = ""

                        try:
                            parse_name_start = str(i).index("name=\"")
                            parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))
                            
                            for ii in range(parse_name_start + 6, parse_name_end):
                                form_name = form_name + str(i)[ii]

                            form_list.append(form_name)

                        except:
                            pass

                    if "query" in str(i):
                        form_name = ""

                        try:
                            parse_name_start = str(i).index("name=\"")
                            parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))
                            
                            for ii in range(parse_name_start + 6, parse_name_end):
                                form_name = form_name + str(i)[ii]

                            form_list.append(form_name)

                        except:
                            pass

                    if "search" in str(i):
                        form_name = ""

                        try:
                            parse_name_start = str(i).index("name=\"")
                            parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                            for ii in range(parse_name_start + 6, parse_name_end):
                                form_name = form_name + str(i)[ii]

                            form_list.append(form_name)

                        except:
                            pass

                    if "tel" in str(i):
                        form_name = ""

                        try:
                            parse_name_start = str(i).index("name=\"")
                            parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                            for ii in range(parse_name_start + 6, parse_name_end):
                                form_name = form_name + str(i)[ii]

                            form_list.append(form_name)

                        except:
                            pass

                    if "text" in str(i):
                        form_name = ""

                        try:
                            parse_name_start = str(i).index("name=\"")
                            parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                            for ii in range(parse_name_start + 6, parse_name_end):
                                form_name = form_name + str(i)[ii]

                            form_list.append(form_name)

                        except:
                            pass

                    if "url" in str(i):
                        form_name = ""

                        try:
                            parse_name_start = str(i).index("name=\"")
                            parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                            for ii in range(parse_name_start + 6, parse_name_end):
                                form_name = form_name + str(i)[ii]

                            form_list.append(form_name)

                        except:
                            pass

                form_list = list(dict.fromkeys(form_list))
                form_list.sort()

                for forms in form_list:
                    for mal in mal_sql:
                        form_dict = {forms: mal}

                        print("checking form (" + mal + "): " + forms)

                        if termux_tor_boolean == True or tor_boolean == True:
                            send_data = web_session.post(j, data = form_dict, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = (5, 30))

                        if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                            send_data = web_session.post(j, data = form_dict, verify = valid_certificate, headers = user_agent, timeout = (5, 30))

                        for i in error_mesage:
                            my_regex = re.search(i, send_data.text)
                            my_boolean = False

                            try:
                                if my_regex:
                                        my_boolean = True
                                        break

                            except UnicodeDecodeError:
                                continue

                        if my_boolean == True:
                            print("true: " + url + " form: " + forms)
                            my_list.append(url + " form: " + forms)

                        if termux_tor_boolean == True or tor_boolean == True:
                            get_data = web_session.get(j, params = form_dict, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = (5, 30))

                        if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                            get_data = web_session.get(j, params = form_dict, verify = valid_certificate, headers = user_agent, timeout = (5, 30))

                        for i in error_mesage:
                            my_regex = re.search(i, get_data.text)
                            my_boolean = False

                            try:
                                if my_regex:
                                        my_boolean = True
                                        break

                            except UnicodeDecodeError:
                                continue

                        if my_boolean == True:
                            print("true: " + url + " form: " + forms)
                            my_list.append(url + " form: " + forms)

            except requests.exceptions.SSLError:
                print("ERROR: invalid certificate!")
                continue

            except urllib3.exceptions.LocationParseError:
                print("ERROR: location parse error!")
                continue

            except requests.exceptions.ConnectionError:
                print("ERROR: connection error!")
                continue

            except requests.exceptions.ConnectTimeout:
                print("ERROR: connect timeout!")
                continue

            except requests.exceptions.InvalidSchema:
                print("ERROR: invalid schema!")
                continue

            except requests.exceptions.InvalidURL:
                print("ERROR: invalid url!")
                continue

            except requests.exceptions.MissingSchema:
                print("ERROR: missing schema!")
                continue

            except requests.exceptions.TooManyRedirects:
                print("ERROR: too many redirects!")
                continue

            except requests.exceptions.ReadTimeout:
                print("ERROR: read timeout!")
                continue

    clear()
    
    return my_list
