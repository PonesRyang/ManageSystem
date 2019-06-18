from rest_framework import serializers

from port.models import Scheduling, Role, EventType, User, UserRole, UserScheduling, Event, Leave


class SchedulingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scheduling
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = '__all__'


class UserRoleSerializer(serializers.ModelSerializer):
    # role = serializers.SerializerMethodField()
    #
    # @staticmethod
    # def get_role(user_role):
    #     return RoleSerializer(user_role.role).data

    class Meta:
        model = UserRole
        fields = 'role',


class UserSerializer(serializers.ModelSerializer):
    # roles = serializers.SerializerMethodField()
    #
    # @staticmethod
    # def get_roles(user):
    #     queryset = UserRole.objects.filter(user=user)
    #     return UserRoleSerializer(queryset,many=True).data

    class Meta:
        model = User
        fields = '__all__'


class UserSchedulingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserScheduling
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = '__all__'