details ={}
details['batchs']=['pfs6','da']
details['students_pfs'] = ['dileep','loki','suma']
details['students_da'] = ['sarath','laxmi','janu']
details.update
details.update({'Name_of_inistute' : ('codegnan'),'branch':('vizag'),
                'subjects':{'python','aptitude','softskills','My-SQL'}})
details.update({'students_pfs_id_numbers' :
                ('CGCVI201','CGCVI202','CGCVI203'),
                'students_da_id_numbers':('CGCVI301','CGCVI302',
                'CGCVI303')})
details['students_pfs'].extend(['anil'])
details['students_da'].extend(['rakesh'])

details.update({'daily_exams_time': ('7 PM to 11 PM'),'Daily_exams' : ('every_day_evening'),
                'marks_out_of' : (30)})
details['psf_students_marks'] = [25,24,30]
details['da_students_marks'] = [26,28,29]

details.update({'day' : ('every_tuesday'),
                'marks_out_of' : (60)})
details['students_pfs_weekly_exam_marks'] = [60,56,50,52]
details['students_da_weekly_exam marks'] = [59,54,53,51]


details.update({'mock_interviews' : ('every_sunday'),
                'marks_out_of' : (10)})
details.update({'students_marks_pfs' : [10,8,9,7],
                'students_marks_da' : [7,8,10,9]})




print(details)


