//
// Created by Rus Ilie Daniel on 26/03/2024.
//

#include "validator.h"

ValidationException::ValidationException(std::string &_message): message(_message) {}

const char* ValidationException::what() const noexcept {
    return message.c_str();
}
EventValidator::EventValidator() = default;

bool EventValidator::validateString(const std::string& input) {
    for (char i : input)
        if (isdigit(i) != false)
            return false;
    return true;
}

void EventValidator::validateTitle(const std::string& title) {
    std::string errors;
    if (!validateString(title))
        errors += std::string("The title input contains digits!");
    if (title.length() == 0)
        errors += std::string("The title input is empty!");
    if (!errors.empty())
        throw ValidationException(errors);
}

void EventValidator::validateDescription(const std::string& description) {
    std::string errors;
    if (!validateString(description))
        errors += std::string("The description input contains digits!");
    if (description.length() == 0)
        errors += std::string("The description input is empty!");
    if (!errors.empty())
        throw ValidationException(errors);
}

void EventValidator::validateYearString(const std::string& year) {
    std::string errors;
    if (year.empty())
        errors += std::string("The year input is empty!");
    if (year.find_first_not_of("0123456789") != std::string::npos)
        errors += std::string("The year input has non-digit characters!");
    if(!errors.empty())
        throw ValidationException(errors);
}

void EventValidator::validateYear(int year) {
    std::string errors;
    if (year<0)
        errors += std::string("year cannot be smaller than 0!");
    if(!errors.empty())
        throw ValidationException(errors);
}

void EventValidator::validateMonthString(const std::string& month) {
    std::string errors;
    if (month.empty())
        errors += std::string("The month input is empty!");
    if (month.find_first_not_of("0123456789") != std::string::npos)
        errors += std::string("The month input has non-digit characters!");
    if(!errors.empty())
        throw ValidationException(errors);
}

void EventValidator::validateMonth(int month) {
    std::string errors;
    if (month<0)
        errors += std::string("Month cannot be smaller than 0!");
    if(!errors.empty())
        throw ValidationException(errors);
}

void EventValidator::validateDayString(const std::string& day) {
    std::string errors;
    if (day.empty())
        errors += std::string("The day input is empty!");
    if (day.find_first_not_of("0123456789") != std::string::npos)
        errors += std::string("The day input has non-digit characters!");
    if(!errors.empty())
        throw ValidationException(errors);
}

void EventValidator::validateDay(int day) {
    std::string errors;
    if (day<0)
        errors += std::string("Day cannot be smaller than 0!");
    if(!errors.empty())
        throw ValidationException(errors);
}

void EventValidator::validateHourString(const std::string& hour) {
    std::string errors;
    if (hour.empty())
        errors += std::string("The hour input is empty!");
    if (hour.find_first_not_of("0123456789") != std::string::npos)
        errors += std::string("The hour input has non-digit characters!");
    if(!errors.empty())
        throw ValidationException(errors);
}

void EventValidator::validateHour(int hour) {
    std::string errors;
    if (hour<0)
        errors += std::string("hour cannot be smaller than 0!");
    if(!errors.empty())
        throw ValidationException(errors);
}

void EventValidator::validateMinuteString(const std::string& minute) {
    std::string errors;
    if (minute.empty())
        errors += std::string("The minute input is empty!");
    if (minute.find_first_not_of("0123456789") != std::string::npos)
        errors += std::string("The minute input has non-digit characters!");
    if(!errors.empty())
        throw ValidationException(errors);
}

void EventValidator::validateMinute(int minute) {
    std::string errors;
    if (minute<0)
        errors += std::string("minute cannot be smaller than 0!");
    if(!errors.empty())
        throw ValidationException(errors);
}

void EventValidator::validateNumberOfPeopleString(const std::string& numberOfPeople) {
    std::string errors;
    if (numberOfPeople.empty())
        errors += std::string("The number of people input is empty!");
    if (numberOfPeople.find_first_not_of("0123456789") != std::string::npos)
        errors += std::string("The number of people input has non-digit characters!");
    if(!errors.empty())
        throw ValidationException(errors);
}

void EventValidator::validateNumberOfPeople(int numberOfPeople) {
    std::string errors;
    if (numberOfPeople<0)
        errors += std::string("number of people cannot be smaller than 0!");
    if(!errors.empty())
        throw ValidationException(errors);
}

void EventValidator::validateLink(const std::string& link) {
    std::string errors;
    if (link.length() == 0)
        errors += std::string("The link input is empty!");
    if (link.find("www") == std::string::npos)
        errors += std::string("The link is not a valid one!");
    if(!errors.empty())
        throw ValidationException(errors);
}

EventValidator::~EventValidator()=default;
