from django.contrib import admin
from .models import Department, Class, Student, Attendance, Course, Teacher, Assign, AssignTime, AttendanceClass
from .models import AttendanceTotal, StudentCourse, Marks, MarksClass, User
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class ClassInline(admin.TabularInline):
    model = Class
    extra = 0


class DeptAdmin(admin.ModelAdmin):
    inlines = [ClassInline]
    list_display = ('name', 'id')
    search_fields = ('name', 'id')
    ordering = ['name']


class StudentInline(admin.TabularInline):
    model = Student
    extra = 0


class ClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'department', 'sem', 'section')
    search_fields = ('id', 'department__name', 'sem', 'section')
    ordering = ['department__name', 'sem', 'section']
    inlines = [StudentInline]


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'department')
    search_fields = ('id', 'name', 'department__name')
    ordering = ['department', 'id']


class AssignTimeInline(admin.TabularInline):
    model = AssignTime
    extra = 0


class AssignAdmin(admin.ModelAdmin):
    inlines = [AssignTimeInline]
    list_display = ('class_id', 'course', 'teacher')
    search_fields = ('class_id__department__name', 'class_id__id', 'course__name', 'teacher__name', 'course__shortname')
    ordering = ['class_id__department__name', 'class_id__id', 'course__id']
    raw_id_fields = ['class_id', 'course', 'teacher']


class MarksInline(admin.TabularInline):
    model = Marks
    extra = 0


class StudentCourseAdmin(admin.ModelAdmin):
    inlines = [MarksInline]
    list_display = ('student', 'course',)
    search_fields = ('student__name', 'course__name', 'student__class_id__id', 'student__class_id__dept__name')
    ordering = ('student__class_id__department__name', 'student__class_id__id', 'student__EID')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('EID', 'name', 'class_id')
    search_fields = ('EID', 'name', 'class_id__id', 'class_id__department__name','email','phone','a_email')
    ordering = ['class_id__department__name', 'class_id__id', 'EID','email','phone','a_email']


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')
    search_fields = ('name', 'department__name')
    ordering = ['department__name', 'name']


admin.site.register(User, UserAdmin)
admin.site.register(Department, DeptAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Assign, AssignAdmin)
admin.site.register(StudentCourse, StudentCourseAdmin)
