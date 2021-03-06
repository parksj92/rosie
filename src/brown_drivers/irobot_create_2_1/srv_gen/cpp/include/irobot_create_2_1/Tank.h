/* Auto-generated by genmsg_cpp for file /home/rbtying/humanoids/src/brown_drivers/irobot_create_2_1/srv/Tank.srv */
#ifndef IROBOT_CREATE_2_1_SERVICE_TANK_H
#define IROBOT_CREATE_2_1_SERVICE_TANK_H
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
struct TankRequest_ {
  typedef TankRequest_<ContainerAllocator> Type;

  TankRequest_()
  : clear(false)
  , left(0)
  , right(0)
  {
  }

  TankRequest_(const ContainerAllocator& _alloc)
  : clear(false)
  , left(0)
  , right(0)
  {
  }

  typedef uint8_t _clear_type;
  uint8_t clear;

  typedef int16_t _left_type;
  int16_t left;

  typedef int16_t _right_type;
  int16_t right;


  typedef boost::shared_ptr< ::irobot_create_2_1::TankRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::irobot_create_2_1::TankRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct TankRequest
typedef  ::irobot_create_2_1::TankRequest_<std::allocator<void> > TankRequest;

typedef boost::shared_ptr< ::irobot_create_2_1::TankRequest> TankRequestPtr;
typedef boost::shared_ptr< ::irobot_create_2_1::TankRequest const> TankRequestConstPtr;



template <class ContainerAllocator>
struct TankResponse_ {
  typedef TankResponse_<ContainerAllocator> Type;

  TankResponse_()
  : success(false)
  {
  }

  TankResponse_(const ContainerAllocator& _alloc)
  : success(false)
  {
  }

  typedef uint8_t _success_type;
  uint8_t success;


  typedef boost::shared_ptr< ::irobot_create_2_1::TankResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::irobot_create_2_1::TankResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct TankResponse
typedef  ::irobot_create_2_1::TankResponse_<std::allocator<void> > TankResponse;

typedef boost::shared_ptr< ::irobot_create_2_1::TankResponse> TankResponsePtr;
typedef boost::shared_ptr< ::irobot_create_2_1::TankResponse const> TankResponseConstPtr;


struct Tank
{

typedef TankRequest Request;
typedef TankResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct Tank
} // namespace irobot_create_2_1

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::irobot_create_2_1::TankRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::irobot_create_2_1::TankRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::irobot_create_2_1::TankRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "c7893eae2d5c5450b4f137c7c7f29b99";
  }

  static const char* value(const  ::irobot_create_2_1::TankRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xc7893eae2d5c5450ULL;
  static const uint64_t static_value2 = 0xb4f137c7c7f29b99ULL;
};

template<class ContainerAllocator>
struct DataType< ::irobot_create_2_1::TankRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "irobot_create_2_1/TankRequest";
  }

  static const char* value(const  ::irobot_create_2_1::TankRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::irobot_create_2_1::TankRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "bool clear\n\
int16 left\n\
int16 right\n\
\n\
";
  }

  static const char* value(const  ::irobot_create_2_1::TankRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::irobot_create_2_1::TankRequest_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::irobot_create_2_1::TankResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::irobot_create_2_1::TankResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::irobot_create_2_1::TankResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "358e233cde0c8a8bcfea4ce193f8fc15";
  }

  static const char* value(const  ::irobot_create_2_1::TankResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x358e233cde0c8a8bULL;
  static const uint64_t static_value2 = 0xcfea4ce193f8fc15ULL;
};

template<class ContainerAllocator>
struct DataType< ::irobot_create_2_1::TankResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "irobot_create_2_1/TankResponse";
  }

  static const char* value(const  ::irobot_create_2_1::TankResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::irobot_create_2_1::TankResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "bool success\n\
\n\
\n\
";
  }

  static const char* value(const  ::irobot_create_2_1::TankResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::irobot_create_2_1::TankResponse_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::irobot_create_2_1::TankRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.clear);
    stream.next(m.left);
    stream.next(m.right);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct TankRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::irobot_create_2_1::TankResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.success);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct TankResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<irobot_create_2_1::Tank> {
  static const char* value() 
  {
    return "745f1885a9f717c8b4a13cfddf382c30";
  }

  static const char* value(const irobot_create_2_1::Tank&) { return value(); } 
};

template<>
struct DataType<irobot_create_2_1::Tank> {
  static const char* value() 
  {
    return "irobot_create_2_1/Tank";
  }

  static const char* value(const irobot_create_2_1::Tank&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<irobot_create_2_1::TankRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "745f1885a9f717c8b4a13cfddf382c30";
  }

  static const char* value(const irobot_create_2_1::TankRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<irobot_create_2_1::TankRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "irobot_create_2_1/Tank";
  }

  static const char* value(const irobot_create_2_1::TankRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<irobot_create_2_1::TankResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "745f1885a9f717c8b4a13cfddf382c30";
  }

  static const char* value(const irobot_create_2_1::TankResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<irobot_create_2_1::TankResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "irobot_create_2_1/Tank";
  }

  static const char* value(const irobot_create_2_1::TankResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // IROBOT_CREATE_2_1_SERVICE_TANK_H

