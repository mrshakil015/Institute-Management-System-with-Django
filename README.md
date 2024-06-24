# Institute Management System with Django

Documentation Link: https://docs.google.com/document/d/16DTSIH5HFTdwWlFqAwML-Kc5qk9h14d5fIJ9e9IPE7M/edit?usp=sharing

## IMSUserModel
- username
- UserType(Authority, Student, Teacher, Staff)
- password
- email

## PersonalInfoModel
- Imsuser
- FatherName
- MotherName
- Religion
- DOB
- Gender
- Mobile
- EmergencyContact
- PresentAddress
- PermanentAddress

## CourseInfoModel
- CourseName
- CourseDuration
- WeeklyClass
- ClassDurationHour
- ClassDurationMinute
- CourseFee
- AboutCourse
- CourseTopics
- CourseImage

## StudentModel
- Imsuser(OneToField Relation with IMSUserModel)
- StudentName
- StudentPhoto
- AdmissionDate
- EducationalQualification
- LinkedInLink
- GithubLink
- FacebookLink

## BatchInfoModel
- Batchuser(Foreginkey Relation with StudentModel)
- BatchNo
- Batchschedule
- Status
- BatchStartDate
- TotalStudent
- BatchInstructor

## TeacherModel
- Imsuser(OneToField Relation with IMSUserModel)
- EmployID
- TeacherName
- Designation
- Skills
- LinkedInLink
- GithubLink
- FacebookLink

## AdmittedCourseModel
- Courseuser(OneToOne Relation with StudentModel)
- AssignTeacher(Foreginkey Relation with TeacherModel)
- LearningBatch(OneToOne Relation with BatchInfoModel)
- CourseName(Foreginkey Relation with CourseInfoModel)
- CourseFee
- Payment
- Due
- AdmissionDate

## StaffModel
- Imsuser(OneToField Relation with IMSUserModel)
- EmployID
- StaffName
- StaffDesignation
- FatherName
- MotherName
- Religion
- DOB
- Gender
- Email
- Mobile
- EmergencyContact
- PresentAddress
- PermanentAddress

## ‍SalaryModel
- Imsuser(Foreginkey Relation with IMSUserModel)
- Name
- Salary
- PaymentDate

## ContactModel
- Mobile
- Address
- Email
- MapLink
- GithubLink
- FacebookLink
- YoutubeLink
- TwitterLink