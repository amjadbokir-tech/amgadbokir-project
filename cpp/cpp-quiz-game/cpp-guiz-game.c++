#include <iostream>
using namespace std;

int main() {

    int choice;

    cout << "Prisoner 207\n";
    cout << "High security prison\n\n";

    cout << "Q1:\n";
    cout << "1- Join the group\n";
    cout << "2- Refuse\n";
    cin >> choice;

    if (choice != 2) {
        cout << "You lost\n";
        return 0;
    }

    cout << "\nQ2:\n";
    cout << "1- Talk to guard\n";
    cout << "2- Observe quietly\n";
    cin >> choice;

    if (choice != 2) {
        cout << "You lost\n";
        return 0;
    }

    cout << "\nQ3:\n";
    cout << "1- Enter tunnel by day\n";
    cout << "2- Wait for maintenance\n";
    cin >> choice;

    if (choice != 2) {
        cout << "You lost\n";
        return 0;
    }

    cout << "\nQ4:\n";
    cout << "1- Steal tool\n";
    cout << "2- Trade quietly\n";
    cin >> choice;

    if (choice != 2) {
        cout << "You lost\n";
        return 0;
    }

    cout << "\nQ5:\n";
    cout << "1- Move now\n";
    cout << "2- Follow plan\n";
    cin >> choice;

    if (choice != 2) {
        cout << "You lost\n";
        return 0;
    }

    cout << "\nYou escaped\n";
    cout << "WIN\n";

    return 0;
}