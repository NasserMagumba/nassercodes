print("\tPROGRAM FOR COMPUTING AVERAGE AND TOTAL OF 4 VARIOUS SUBJECTS\n")
subject_1_score=int(input("\tEnter subject_1 marks: "))
subject_2_score=int(input("\tEnter subject_2 marks: "))
subject_3_score=int(input("\tEnter subject_3 marks: "))
subject_4_score=int(input("\tEnter subject_4 marks: "))

#computation
total=int(subject_1_score+subject_2_score+subject_3_score+subject_4_score)
average=float(subject_1_score+subject_2_score+subject_3_score+subject_4_score/4)

#output
print(f"total {total}\n average {average}")
