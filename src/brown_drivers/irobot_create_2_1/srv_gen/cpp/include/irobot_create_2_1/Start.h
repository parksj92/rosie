/* Auto-generated by genmsg_cpp for file /home/rbtying/humanoids/src/brown_drivers/irobot_create_2_1/srv/Start.srv */
#ifndef IROBOT_CREATE_2_1_SERVICE_START_H
#define IROBOT_CREATE_2_1_SERVICE_START_H
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
struct StartRequest_ {
  typedef StartRequest_<ContainerAllocator> Type;

  StartRequest_()
  : start(false)
  {
  }

  StartRequest_(const ContainerAllocator& _alloc)
  : start(false)
  {
  }

  typedef uint8_t _start_type;
  uint8_t start;


  typedef boost::shared_ptr< ::irobot_create_2_1::StartRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::irobot_create_2_1::StartRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct StartRequest
typedef  ::irobot_create_2_1::StartRequest_<std::allocator<void> > StartRequest;

typedef boost::shared_ptr< ::irobot_create_2_1::StartRequest> StartRequestPtr;
typedef boost::shared_ptr< ::irobot_create_2_1::StartRequest const> StartRequestConstPtr;



template <class ContainerAllocator>
struct StartResponse_ {
  typedef StartResponse_<ContainerAllocator> Type;

  StartResponse_()
  : success(false)
  {
  }

  StartResponse_(const ContainerAllocator& _alloc)
  : success(false)
  {
  }

  typedef uint8_t _success_type;
  uint8_t success;


  typedef boost::shared_ptr< ::irobot_create_2_1::StartResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::irobot_create_2_1::StartResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct StartResponse
typedef  ::irobot_create_2_1::StartResponse_<std::allocator<void> > StartResponse;

typedef boost::shared_ptr< ::irobot_create_2_1::StartResponse> StartResponsePtr;
typedef boost::shared_ptr< ::irobot_create_2_1::StartResponse const> StartResponseConstPtr;


struct Start
{

typedef StartRequest Request;
typedef StartResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct Start
} // namespace irobot_create_2_1

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::irobot_create_2_1::StartRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::irobot_create_2_1::StartRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::irobot_create_2_1::StartRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "676aa7bfb3ec2071e814f2368dfd5fb5";
  }

  static const char* value(const  ::irobot_create_2_1::StartRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x676aa7bfb3ec2071ULL;
  static const uint64_t static_value2 = 0xe814f2368dfd5fb5ULL;
};

template<class ContainerAllocator>
struct DataType< ::irobot_create_2_1::StartRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "irobot_create_2_1/StartRequest";
  }

  static const char* value(const  ::irobot_create_2_1::StartRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::irobot_create_2_1::StartRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "bool start\n\
\n\
";
  }

  static const char* value(const  ::irobot_create_2_1::StartRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::irobot_create_2_1::StartRequest_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::irobot_create_2_1::StartResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::irobot_create_2_1::StartResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::irobot_create_2_1::StartResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "358e233cde0c8a8bcfea4ce193f8fc15";
  }

  static const char* value(const  ::irobot_create_2_1::StartResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x358e233cde0c8a8bULL;
  static const uint64_t static_value2 = 0xcfea4ce193f8fc15ULL;
};

template<class ContainerAllocator>
struct DataType< ::irobot_create_2_1::StartResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "irobot_create_2_1/StartResponse";
  }

  static const char* value(const  ::irobot_create_2_1::StartResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::irobot_create_2_1::StartResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "bool success\n\
\n\
\n\
";
  }

  static const char* value(const  ::irobot_create_2_1::StartResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::irobot_create_2_1::StartResponse_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::irobot_create_2_1::StartRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.start);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct StartRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::irobot_create_2_1::StartResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.success);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct StartResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<irobot_create_2_1::Start> {
  static const char* value() 
  {
    return "bbb7ba84302b6f35af5466a95cd7ac90";
  }

  static const char* value(const irobot_create_2_1::Start&) { return value(); } 
};

template<>
struct DataType<irobot_create_2_1::Start> {
  static const char* value() 
  {
    return "irobot_create_2_1/Start";
  }

  static const char* value(const irobot_create_2_1::Start&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<irobot_create_2_1::StartRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "bbb7ba84302b6f35af5466a95cd7ac90";
  }

  static const char* value(const irobot_create_2_1::StartRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<irobot_create_2_1::StartRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "irobot_create_2_1/Start";
  }

  static const char* value(const irobot_create_2_1::StartRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<irobot_create_2_1::StartResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "bbb7ba84302b6f35af5466a95cd7ac90";
  }

  static const char* value(const irobot_create_2_1::StartResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<irobot_create_2_1::StartResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "irobot_create_2_1/Start";
  }

  static const char* value(const irobot_create_2_1::StartResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // IROBOT_CREATE_2_1_SERVICE_START_H

