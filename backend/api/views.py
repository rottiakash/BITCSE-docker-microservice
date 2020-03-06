from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.models import TT,Faculty,Slot,Subject,Attendance,Marks,LAB
# Create your views here.
class getTT(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        result = []
        pid = request.user.username
        if(len(pid)==10):
            semsec = self.request.user.profile.semsec
            days = ['MON','TUE','WED','THU','FRI','SAT']
            for day in days:
                subs = TT.objects.filter(semsec=semsec,day=day)
                subl = []
                for sub in subs:
                    subr = {
                        "subcode":sub.subject.subcode,
                        "subname":sub.subject.subname,
                        "faculty":sub.faculty.name,
                        "slot":sub.slot.time,
                        "room":sub.room
                    }
                    subl.append(subr)
                result.append(subl)
            return Response(result)
        else:
            days = ['MON','TUE','WED','THU','FRI','SAT']
            for day in days:
                subs = TT.objects.filter(faculty__fid=pid,day=day)
                subl = []
                for sub in subs:
                    subr = {
                        "subcode":sub.subject.subcode,
                        "subname":sub.subject.subname,
                        "faculty":sub.faculty.name,
                        "slot":sub.slot.time,
                        "room":sub.room
                    }
                    subl.append(subr)
                result[day]=subl
            return Response(result)


class getFaculty(APIView):

    permission_classes = (IsAuthenticated,)
    
    def get(self,request):
        result = []
        for fact in Faculty.objects.all().order_by('fid'):
            res = {
                "fid":fact.fid,
                "name":fact.name,
                "email":fact.email,
                "phone":fact.phone,
                "desg":fact.desg,
                "qual":fact.quali
            }
            result.append(res)
        return Response(result)


class getAttendance(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        result = []
        for attend in Attendance.objects.filter(user__username=self.request.user.username):
            res = {
                "subcode" : attend.subject.subcode,
                "per" : attend.per
            }
            result.append(res)
        return Response(result)

class getMarks(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        result = []
        for mark in Marks.objects.filter(user__username=self.request.user.username):
            res ={
                'subcode':mark.subject.subcode,
                'marks':[mark.Test1,mark.Test2,mark.Test3]
            }
            result.append(res)
        return Response(result)


class getLAB(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        result = []
        pid = request.user.username
        if(len(pid)==10):
            batch = self.request.user.profile.batch
            days = ['MON','TUE','WED','THU','FRI','SAT']
            for day in days:
                subs = LAB.objects.filter(batch=batch,day=day)
                subl = []
                for sub in subs:
                    subr = {
                        "subcode":sub.subject.subcode,
                        "subname":sub.subject.subname,
                        "faculty1":sub.faculty1.name,
                        "faculty2":sub.faculty2.name,
                        "slot":sub.slot.time,
                    }
                    subl.append(subr)
                result.append(subl)
            return Response(result)
        else:
            days = ['MON','TUE','WED','THU','FRI','SAT']
            for day in days:
                subs = LAB.objects.filter(faculty1__fid=pid,day=day) | LAB.objects.filter(faculty2__fid=pid,day=day)
                subl = []
                for sub in subs:
                    subr = {
                        "subcode":sub.subject.subcode,
                        "subname":sub.subject.subname,
                        "faculty1":sub.faculty1.name,
                        "faculty2":sub.faculty2.name,
                        "slot":sub.slot.time,
                    }
                    subl.append(subr)
                result[day]=subl
            return Response(result)