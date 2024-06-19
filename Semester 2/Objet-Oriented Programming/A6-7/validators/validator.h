//
// Created by Rus Ilie Daniel on 26/03/2024.
//

#ifndef A45OOP_VALIDATOR_H
#define A45OOP_VALIDATOR_H
#include "../domain/domain.h"
#include "../domain/datetime.h"

class ValidationException: public std::exception {
private:
    std::string message;
public:
    explicit ValidationException(std::string& _message);

    const char *what() const noexcept override;
};

class EventValidator {
public:
    EventValidator();

    bool validateString(const std::string& input);

    void validateTitle(const std::string& title);

    void validateDescription(const std::string& description);

    void validateYearString(const std::string&year);

    void validateMonthString(const std::string&month);

    void validateDayString(const std::string&day);

    void validateHourString(const std::string&hour);

    void validateMinuteString(const std::string&minute);

    void validateYear(int year);

    void validateMonth(int month);

    void validateDay(int day);

    void validateHour(int hour);

    void validateMinute(int minute);

    void validateNumberOfPeopleString(const std::string& numberOfPeople);

    void validateNumberOfPeople(int numberOfPeople);

    void validateLink(const std::string& link);

    ~EventValidator();
};
#endif //A45OOP_VALIDATOR_H
