// Базовый класс
function StudentBase(lastName, firstName, middleName, gender, age, course) {
    this.lastName = lastName;
    this.firstName = firstName;
    this.middleName = middleName;
    this.gender = gender;
    this.age = age;
    this.course = course;
}

StudentBase.prototype.getFullName = function() {
    return `${this.lastName} ${this.firstName} ${this.middleName}`;
};

StudentBase.prototype.getAge = function() {
    return this.age;
};

StudentBase.prototype.setAge = function(age) {
    if ( age >= 16 && age <= 35) {
        this.age = age;
    } else {
        alert("Возраст должен быть между 16 и 35")
    }
};

StudentBase.prototype.getCourse = function() {
    return this.course;
}

StudentBase.prototype.setCourse = function(course) {
    if ( course >= 1 && course <= 5) {
        this.course = course;
    } else {
        alert("Курс должен быть между 1 и 5");
    }
};

// Класс наследник
function StudentExtended(lastName, firstName, middleName, gender, age, course) {
    StudentBase.call(this, lastName, firstName, middleName, gender, age, course);
    this.gender = gender;
}

StudentExtended.prototype = Object.create(StudentBase.prototype);
StudentExtended.prototype.constructor = StudentExtended;

StudentExtended.prototype.isMale = function() {
    return this.gender === "М";
}

// class/extends
class StudentBaseClass {
    constructor(lastName, firstName, middleName, gender, age, course) {
        this.lastName = lastName;
        this.firstName = firstName;
        this.middleName = middleName;
        this.gender = gender;
        this.age = age;
        this.course = course;
    }

    getFullName() {
        return `${this.lastName} ${this.firstName} ${this.middleName}`;
    }

    getAge() {
        return this.age;
    }

    setAge(age) {
        if ( age >= 16 && age <= 35) {
            this.age = age;
        } else {
            alert("Возраст должен быть между 16 и 35");
        }
    }

    getCourse() {
        return this.course;
    }

    setCourse(course) {
        if ( course >= 1 && course <= 5) {
            this.course = course;
        } else {
            alert("Курс должен быть между 1 и 5")
        }
    }
}

class StudentExtendedClass extends StudentBaseClass {
    constructor(lastName, firstName, middleName, gender, age, course) {
        super(lastName, firstName, middleName, gender, age, course);
    }

    isMale() {
        return this.gender === "М";
    }
}

const initialData = [
    { lastName: "Иванов", firstName: "Иван", middleName: "Иванович", gender: "М", age: 20, course: 3 },
    { lastName: "Петрова", firstName: "Анна", middleName: "Сергеевна", gender: "Ж", age: 22, course: 2 },
    { lastName: "Сидоров", firstName: "Павел", middleName: "Алексеевич", gender: "М", age: 19, course: 1 },
    { lastName: "Смирнов", firstName: "Алексей", middleName: "Игоревич", gender: "М", age: 21, course: 4 },
    { lastName: "Кузнецова", firstName: "Мария", middleName: "Петровна", gender: "Ж", age: 20, course: 3 },
];

// Инициализация массивов студентов для обоих методов
const studentsPrototype = initialData.map(data => new StudentExtended(
    data.lastName,
    data.firstName,
    data.middleName,
    data.gender,
    data.age,
    data.course
));

const studentsClass = initialData.map(data => new StudentExtendedClass(
    data.lastName,
    data.firstName,
    data.middleName,
    data.gender,
    data.age,
    data.course
));

function addStudent() {
    const lastName = document.getElementById("last-name").value;
    const firstName = document.getElementById("first-name").value;
    const middleName = document.getElementById("middle-name").value;
    const gender = document.getElementById("gender").value;
    const age = parseInt(document.getElementById("age").value, 10);
    const course = parseInt(document.getElementById("course").value, 10);

    const studentProto = new StudentExtended(lastName, firstName, middleName, gender, age, course);
    studentsPrototype.push(studentProto);

    const studentClass = new StudentExtendedClass(lastName, firstName, middleName, gender, age, course);
    studentsClass.push(studentClass);

    displayStudentsPrototype();
    displayStudentsClass();
    analyzeStudents();
}

function displayStudentsPrototype() {
    const studentList = document.getElementById("student-list-prototype");
    studentList.innerHTML = "";

    studentsPrototype.forEach((student, index) => {
        const studentDiv = document.createElement("div");
        studentDiv.textContent = `${index + 1}. ${student.getFullName()} - Возраст: ${student.getAge()} - Курс: ${student.getCourse()} - Пол: ${student.gender}`;
        studentList.appendChild(studentDiv);
    });
}

function displayStudentsClass() {
    const studentList = document.getElementById("student-list-class");
    studentList.innerHTML = "";

    studentsClass.forEach((student, index) => {
        const studentDiv = document.createElement("div");
        studentDiv.textContent = `${index + 1}. ${student.getFullName()} - Возраст: ${student.getAge()} - Курс: ${student.getCourse()} - Пол: ${student.gender}`;
        studentList.appendChild(studentDiv);
    });
}

function analyzeStudents() {
    const resultDiv = document.getElementById('analysis-result');
    resultDiv.innerHTML = "";

    const courseStats = {};

    studentsPrototype.forEach((student) => {
        if (!courseStats[student.course]) {
            courseStats[student.course] = { male: 0, total: 0 };
        }

        if (student.isMale()) {
            courseStats[student.course].male++;
        }

        courseStats[student.course].total++;
    });

    let maxPercentage = 0;
    let bestCourse = null;

    for (const [course, stats] of Object.entries(courseStats)) {
        const percentage = (stats.male / stats.total) * 100;
        if (percentage > maxPercentage) {
            maxPercentage = percentage;
            bestCourse = course;
        }
    }

    resultDiv.textContent = bestCourse ? `${bestCourse} курс имеет самый высокий процент мужчин: ${maxPercentage.toFixed(2)}%` : "Нет данных";
}

const addStudentButton = document.getElementById("add-student");
addStudentButton.addEventListener("click", addStudent);