
# -*- coding: utf-8 -*-
"""
사용자들의 문제별 제출 소스 확인 모듈
"""


from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER

from model import Base
from model.members import Members
from model.problems import Problems


class DataOfSubmissionBoard(Base) :
    
    __tablename__ = 'DataOfSubmissionBoard'
    
    submissionIndex = Column(INTEGER(unsigned = True),
                             primary_key = True,
                             autoincrement = True,
                             nullable = False)
    memberIdIndex = Column(INTEGER(unsigned = True),
                           ForeignKey(Members.memberIdIndex,
                                      onupdate = 'CASCADE',
                                      ondelete = 'CASCADE'),
                           nullable = False,
                           unique = True)
    problemIndex = Column(INTEGER(unsigned = True),
                          ForeignKey(Problems.problemIndex,
                                     onupdate = 'CASCADE',
                                     ondelete = 'CASCADE'),
                          nullable = False,
                          unique = True)
    viewCount = Column(INTEGER(unsigned = True),
                       default = 0,
                       nullable = False)
    submissionReplyCount = Column(INTEGER(unsigned = True),
                                   default = 0,
                                   nullable = False)
    sumOfLikeCount = Column(INTEGER(unsigned = True),
                            default = 0,
                            nullable = False)
    
