/* Auto-generated by genmsg_cpp for file /home/rbtying/humanoids/src/brown_drivers/irobot_create_2_1/srv/Turn.srv */
#ifndef IROBOT_CREATE_2_1_SERVICE_TURN_H
#define IROBOT_CREATE_2_1_SERVICE_TURN_H
#include <string>
#include <vector>
#include <map>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/time.h"

#include "ros/macros.h"

#include "ros/assert.h"

#include "ros/service_traits.h"




namespace irobot_create_2_1
{
template <class ContainerAllocator>
struct TurnRequest_ {
  typedef TurnRequest_<ContainerAllocator> Type;

  TurnRequest_()
  : clear(false)
  , turn(0)
  {
  }

  TurnRequest_(const ContainerAllocator& _alloc)
  : clear(false)
  , turn(0)
  {
  }

  typedef uint8_t _clear_type;
  uint8_t clear;

  typedef int16_t _turn_type;
  int16_t turn;


  typedef boost::shared_ptr< ::irobot_create_2_1::TurnRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::irobot_create_2_1::TurnRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct TurnRequest
typedef  ::irobot_create_2_1::TurnRequest_<std::allocator<void> > TurnRequest;

typedef boost::shared_ptr< ::irobot_create_2_1::TurnRequest> TurnRequestPtr;
typedef boost::shared_ptr< ::irobot_create_2_1::TurnRequest const> TurnRequestConstPtr;



template <class ContainerAllocator>
struct TurnResponse_ {
  typedef TurnResponse_<ContainerAllocator> Type;

  TurnResponse_()
  : success(false)
  {
  }

  TurnResponse_(const ContainerAllocator& _alloc)
  : success(false)
  {
  }

  typedef uint8_t _success_type;
  uint8_t success;


  typedef boost::shared_ptr< ::irobot_create_2_1::TurnResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::irobot_create_2_1::TurnResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct TurnResponse
typedef  ::irobot_create_2_1::TurnResponse_<std::allocator<void> > TurnResponse;

typedef boost::shared_ptr< ::irobot_create_2_1::TurnResponse> TurnResponsePtr;
typedef boost::shared_ptr< ::irobot_create_2_1::TurnResponse const> TurnResponseConstPtr;


struct Turn
{

typedef TurnRequest Request;
typedef TurnResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct Turn
} // namespace irobot_create_2_1

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::irobot_create_2_1::TurnRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::irobot_create_2_1::TurnRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::irobot_create_2_1::TurnRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "d7233ced7da7131cf3836ae5864297ef";
  }

  static const char* value(const  ::irobot_create_2_1::TurnRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xd7233ced7da7131cULL;
  static const uint64_t static_value2 = 0xf3836ae5864297efULL;
};

template<class ContainerAllocator>
struct DataType< ::irobot_create_2_1::TurnRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "irobot_create_2_1/TurnRequest";
  }

  static const char* value(const  ::irobot_create_2_1::TurnRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::irobot_create_2_1::TurnRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "bool clear\n\
int16 turn\n\
\n\
";
  }

  static const char* value(const  ::irobot_create_2_1::TurnRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::irobot_create_2_1::TurnRequest_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::irobot_create_2_1::TurnResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::irobot_create_2_1::TurnResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::irobot_create_2_1::TurnResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "358e233cde0c8a8bcfea4ce193f8fc15";
  }

  static const char* value(const  ::irobot_create_2_1::TurnResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x358e233cde0c8a8bULL;
  static const uint64_t static_value2 = 0xcfea4ce193f8fc15ULL;
};

template<class ContainerAllocator>
struct DataType< ::irobot_create_2_1::TurnResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "irobot_create_2_1/TurnResponse";
  }

  static const char* value(const  ::irobot_create_2_1::TurnResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::irobot_create_2_1::TurnResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "bool success\n\
\n\
\n\
";
  }

  static const char* value(const  ::irobot_create_2_1::TurnResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::irobot_create_2_1::TurnResponse_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::irobot_create_2_1::TurnRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.clear);
    stream.next(m.turn);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct TurnRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::irobot_create_2_1::TurnResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.success);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct TurnResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<irobot_create_2_1::Turn> {
  static const char* value() 
  {
    return "f28782ca6cac906741095df052f0ccc1";
  }

  static const char* value(const irobot_create_2_1::Turn&) { return value(); } 
};

template<>
struct DataType<irobot_create_2_1::Turn> {
  static const char* value() 
  {
    return "irobot_create_2_1/Turn";
  }

  static const char* value(const irobot_create_2_1::Turn&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<irobot_create_2_1::TurnRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "f28782ca6cac906741095df052f0ccc1";
  }

  static const char* value(const irobot_create_2_1::TurnRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<irobot_create_2_1::TurnRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "irobot_create_2_1/Turn";
  }

  static const char* value(const irobot_create_2_1::TurnRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<irobot_create_2_1::TurnResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "f28782ca6cac906741095df052f0ccc1";
  }

  static const char* value(const irobot_create_2_1::TurnResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<irobot_create_2_1::TurnResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "irobot_create_2_1/Turn";
  }

  static const char* value(const irobot_create_2_1::TurnResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // IROBOT_CREATE_2_1_SERVICE_TURN_H
