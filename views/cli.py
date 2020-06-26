from controllers.list_controller import ListController
class CLI:
    def __init__(self):
        controller = ListController()
    

        while True:
            line = input()

            if line == "":
                exit(0)

            commands = line.split(" ")

            if commands[0] == "RP":
                categoria = commands[1]
                nome_profissional = commands[2]
                if not controller.has_categoria(categoria):
                    print('Categoria inexistente.')
                elif controller.has_profissional(categoria, nome_profissional):
                    print('Profissional existente.')
                else:
                    controller.add_profissional(categoria, nome_profissional)
                    print('Profissional registado com sucesso.')

            elif commands[0] == "RU":
                nome_utente = commands[1]
                faixa_etaria = commands[2]
                if controller.has_utente(nome_utente):
                    print('Utente existente.')
                elif not controller.has_faixa(faixa_etaria):
                    print('Faixa etaria inexistente.')
                else:
                    print('Utente registado com sucesso.')
            
            elif commands[0] == "RF":
                name_family = commands[1]
                if not controller.has_family(nome_familia):
                    print('Família existente.')
                else:
                    print('Família registada com sucesso.')
            
            elif commands[0] == "AF":
                nome_utente = commands[1]
                nome_familia = commands[2]
                if not controller.has_utente(nome_utente):
                    print('Utente inexistente.')
                elif not controller.has_family(nome_familia):
                    print('Família inexistente.')
                elif not controller.exist_family(nome_familia):
                    print('Utente pertence a família.')
                else:
                    print('Utente associado a família.')

            elif commands[0] == "DF":
                nome_utente = commands[1]
                if not controller.has_utente(nome_utente):
                    print('Utente inexistente')
                elif not controller.has_family(nome_utente):
                    print("Utente não pertence a família.")
                else:
                    controller.remove_user_family()
                    print('Utente desassociado de família')

            elif commands[0] == "LP":
                #listar todos os profissionais de saude por categoria e por ordem alfabética dentro de cada categoria
                if not controller.has_utente_in_table():
                    print('Sem profissionais registado.')
                else:
                    controller.print_list_professionals()

            
            elif commands[0] == "LU":
                #listar todos os utentes por faixa etária, por ordem alfabética de família em cada faixa etária e por ordem de nome dentro de cada 
                # familia 
                if not cotroller.has_utente_in_table():
                    print('Sem utentes registados.')                
                else:
                    cotroller.print_list_users()


            elif commands[0] == "LF":
                #listar todas as famílias por ordem alfabética.
                if not controller.has_family_register():
                    print('Sem famílias registadas.')
                else:
                    controller.print_families()

            elif commands[0] == "MF":
                # lista todos os utentes de uma família, por ordem de faixa etária, e por ordem alfabética dentro de cada faixa etária.
                # as faixas etárias devem ser listadas de acordo com a ordem na tabela 2

                nome_familia = commands[1]
                if not controller.has_family(nome_familia):
                    print('Familia inexistente')
                else:
                    controller.print_users_family()

            elif commands[0] == "MC": pass


            elif commands[0] == "CC":
                # cancelar os cuidados de saúde marcados a um utente
                nome_utente = commands[1]
                if not controller.has_utente(nome_utente):
                    print('Utente inexistente.')
                elif not controller.existe_cuidado(nome_utente):
                    print('Utente sem cuidados de saúde marcados.')
                else:
                    controller.desmarcar_cuidado(nome_utente)


            elif commands[0] == "LCU":
                # listar todos os serviços marcados a um utente, por ordem de serviço, por ordem de categoria por 
                # ordem alfabética de node de profissional por cada categoria.
                nome_utente =commands[1]
                if not controller.has_utente(nome_utente):
                    print('Utente inexistente.')
                elif not controller.existe_cuidado(nome_utente):
                    print('Utente sem cuidados de saúde marcados.')
                else:
                    controller.listar_cuidados_utente(nome_utente)


            elif commands[0] == "LCF":
                nome_familia = commands[1]
                if not controller.has_family(nome_familia):
                    print('Família inexistente.')
                elif not controller.existe_cuidado(nome_familia):
                    print('Família sem cuidados de saúde marcados.')
                else:
                    controller.listar_cuidados_familia(nome_familia)

            elif commands[0] == "LSP":
                #listar todos os serviços marcados a um profissional de saude, por ordem de tipo de serviço, e por ordem
                # alfabética de nome de utente por tipo de serviço.
                categoria = commands[1]
                nome_profissional = commands[2]
                if not controller.has_profissional(nome_profissional):
                    print('Profissional de saúde inexistente.')
                elif not controller.listar_cuidados_profissional(nome_profissional):
                    print('Profissional de saúde sem marcações.')
                else:
                    controller.listar_cuidados_prof(nome_profissional)

                
            elif commands[0] == "LMS":
                serviço = commands[1]
                if not controller.has_service(serviço):
                    print('Serviço inexistente')
                elif not controller.has_marked_service(serviço):
                    print('Serviço sem marcações.')
                else:
                    controller.list_marked_services(serviço)
                    

            elif commands[0] == "G": pass

            elif commands[0] == "L": pass


            else:
                print("Instrução inválida.")