import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Storage from '@mui/icons-material/Storage';
import { Link } from 'react-router-dom';
import TableViewIcon from '@mui/icons-material/TableView';
import SchoolIcon from '@mui/icons-material/School';
import { Divider } from '@mui/material';
const List = [
  { icon: <Storage color='primary'/>, title: 'Chat DB', description: '使用自然的语言操作数据库', href: '/chat/db/new' },
  { icon: <TableViewIcon color='success'/>, title: 'Chat Excel', description: '使用自然的语言与EXCEL对话', href: '/chat/excel/new' },
  { icon: <SchoolIcon  color='secondary'/>, title: 'Chat Knowledge', description: '向知识库提出问题&得到答案', href: '/chat/knowledge/new' },
];
export function ChatSelect() {
  return (
    <>
      <div className="max-w-3xl m-auto flex justify-center items-center w-full h-full">
        {/* <Divider className='pb-8'>快速开始</Divider> */}
        <div className="grid grid-cols-1 grid-col-1 gap-4 flex-1">
          {List.map((item, index) => {
            return (
              <Link to={item.href} key={index}>
                <div className="cursor-pointer">
                  <Card sx={{ '&:hover': { boxShadow: 6 } }}>
                    <CardContent>
                      <div className="flex gap-4">
                        <div>
                          <div>{item.icon}</div>
                        </div>
                        <div className="flex-1 flex flex-col gap-4">
                          <div>{item.title}</div>
                          <div>{item.description}</div>
                        </div>
                      </div>
                    </CardContent>
                  </Card>
                </div>
              </Link>
            );
          })}
        </div>
      </div>
    </>
  );
}
