# Classes

Referência para organização de arquivos: https://www.learncpp.com/cpp-tutorial/89-class-code-and-header-files/

## Domínios
### 1 Temporalidade
#### 1.1 Data
```
class Date {
private:
    short day;
    short month;
    short year;

    void validate() {
        // checar se é número
        // checar números negativos
        // se isBisectYear()
        //  check day number;
    }

public:
    void set(string);
    void set(int, int, int);

    // ou fazer __repr__ ?
    string get() {
        return day +"/"+ month +"/"+ year;
    }
}
```

#### 1.2 Horário
```
class Hours {
private:
    short hours;
    shoort minutes;

    void validate() {
        // checar se é número
        // checar números negativos
        // se isBisectYear()
        //  check day number;
    }

    void checkForBisect() {
        // do the math
    }

public:
    void set(string);
    void set(int, int, int);

    // ou fazer __repr__ ?
    strign get() {
        return hours +"H"+ minutes;
    }
}
```

### 2 Localidade
#### 2.1 Cidade
`class City`
#### 2.2 Estado
`class State`

### 3 Códigos
```cpp
class Code
    // se eu definir um construtor pra essa classe abstrata, 
    // ainda não seria possível instanciar um obj dessa classe?
    string code;
    int length; //?
    abstract bool validate();
```
#### 3.1 Código de Evento
`class EventCode extends Code`

#### 3.2 Código de Apresentação
`class PresentationCode extends Code`

#### 3.2 Código de Ingresso
`class TicketCode extends Code`

### Usuário
class Password
class Cpf

<hr>


## Entidades
Aí vem uma lista de entidades.