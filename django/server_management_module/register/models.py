from django.db import models

class Profile(models.Model):
    COLLEGES = [
            ('COA', 'College of Agriculture'),
            ('CBAA', 'College of Business Administration and Accountancy'),
            ('CED', 'College of Education'),
            ('COE', 'College of Engineering'),
            ('DET', 'Division of Engineering Technology'),
            ('COF', 'College of Fisheries'),
            ('CFES', 'College of Forestry and Environmental Studies'),
            ('CHS', 'College of Health Sciences'),
            ('CHARM', 'College of Hotel and Restaurant Management'),
            ('CICS', 'College of Information and Computing Sciences'),
            ('CNSM', 'College of Natural Sciences and Mathematics'),
            ('CPA', 'College of Public Affairs'),
            ('CSSH', 'College of Social Sciences and Humanities'),
            ('CSPEAR', 'College of Sports, Physical Education and Recreation'),
            ('KFCFIAAS', 'King Faisal Center for Islamic, Arabic and Asian Studies'),
            ('COL', 'College of Law'),
            ('COM', 'College of Medicine'),
            ('GS', 'Graduate School'),
            ]

    COURSES = [
        ('ABM', 'Bachelor of Science in Agricultural Business Management'),
        ('BSAA', 'BSA Agronomy'),
        ('BSAAS', 'BSA Animal Science'),
        ('BSAEE', 'BSA major in Extension Education'),
        ('BSAFS', 'BSA Farming Systems'),
        ('BSABSE', 'Bachelor of Science in Agricultural and Bio Systems Engineering'),
        ('BSAH', 'BSA Horticulture'),
        ('BSAAFP', 'BSA Agricultural Food Processing'),
        ('DATCP', 'DAT Crop Production'),
        ('DABMTFP', 'DABMT Food Processing'),

        ('BSA', 'Bachelor of Science in Accountancy'),
        ('BSBABE', 'Bachelor of Science in Business Administration Business Economics'),
        ('BSBAM', 'Bachelor of Science in Business Administration Management'),
        ('BSBAHRM', 'Bachelor of Science in Business Administration Human Resource Management'),
        ('BSBAEM', 'Bachelor of Science in Business Administration Entrepreneurial Marketing'),
        ('BSBAE', 'Bachelor of Science in Business Administration Entrepreneurship'),

        ('BSEDB', 'Bachelor of Secondary Education Biology'),
        ('BSEDE', 'Bachelor of Secondary Education English'),
        ('BSEDF', 'Bachelor of Secondary Education Filipino'),
        ('BSEDH', 'Bachelor of Secondary Education History'),
        ('BSEDM', 'Bachelor of Secondary Education Mathematics'),
        ('BSEDP', 'Bachelor of Secondary Education Physics'),
        ('BSEDTLE', 'Bachelor of Secondary Education Technology and Livelihoood Education'),
        ('BSEDS', 'Bachelor of Secondary Education Sciences'),
        ('BSEDSS', 'Bachelor of Secondary Education Social Studies'),
        ('BEEDEVED', 'Bachelor of Elementary Education major in Early Childhood Education and Development'),
        ('BEEDGE', 'Bachelor of Elementary Education major in General Education'),
        ('BTVEDHE', 'BTVED Home Econonomics'),
        ('BTLET', 'Bachelor of Technology and Livelihood Education major in Home Economics'),

        ('BSChemE', 'Bachelor of Science in Chemical Engineering'),
        ('BSCE', 'Bachelor of Science in Civil Engineering'),
        ('BSECE', 'Bachelor of Science in Electronics and Communications Engineering'),
        ('BSEE', 'Bachelor of Science in Electrical Engineering'),
        ('BSME', 'Bachelor of Science in Mechanical Engineering'),

        ('BSETCEM', 'Bachelor of Science in Engineering Technology (Construction Engineering Management)'),
        ('BSETERE', 'Bachelor of Science in Engineering Technology (Electrical and RenewableEnergy)'),
        ('BSETMF', 'Bachelor of Science in Engineering Technology (Machining and Fabrication)'),
        ('DITCT', 'Diploma in Technology major in Construction Technology'),
        ('DITMST', 'Diploma in Technology major in Machine Shop Technology'),

        ('BSF', 'Bachelor of Science in Fisheries'),
        ('DITFP', 'Diploma in Technology major in Fish Processing'),
        ('DITA', 'Diploma in Technology major in Acquaculture'),

        ('BSF', 'Bachelor of Science in Forestry'),
        ('BSFAF', 'Bachelor of Science in Forestry major in Agroforestry'),
        ('BSES', 'Bachelor of Science in Environmental Science'),

        ('BSHM', 'Bachelor of Science in Hospitality Management'),
        ('BSTM', 'Bachelor of Science in Tourism Management'),
        ('BSCS', 'Bachelor of Science in Computer Science'),
        ('BSIS', 'Bachelor of Science in Information System'),
        ('BSEMC', 'Bachelor of Science in Entertainment and Multimedia Computing'),
        ('BSIT', 'Bachelor of Science in Information Technology (Major in Networking, Database System'),
        ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,default=None)
    college = models.CharField(max_length=50)
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name


class User(models.Model):

    USER_TYPE = [
            ('0', 'Faculty'),
            ('1', 'Student'),
            ]

    profile_id = models.OneToOneField(
            Profile,
            on_delete=models.CASCADE)
    usertype = models.CharField(max_length=50)
    mac_address = models.CharField(max_length=50)
    blocked = models.BooleanField(default=False)


    def __str__(self):
        return str(self.profile_id)
