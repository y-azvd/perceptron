## Classes

referencia: https://www.learncpp.com/cpp-tutorial/89-class-code-and-header-files/

### Domains - "time"
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

class Hours /* ??? */ {
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

## Domains - location
class State
class City

## Domains - codes
class Code
    // se eu definir um construtor pra essa classe abstrata, 
    // ainda não seria possível instanciar um obj dessa classe?
    string code;
    int length; //?
    abstract bool validate();

class EventCode extends Code
class PresentationCode extends Code
class TicketCode extends Code

## Domains - password
## Domains - CPF
