import React, { useState, useEffect } from 'react';
import {
    AppBar, Box, Button, Card, CardActions, CardContent, CardHeader, CardMedia, CircularProgress,
    Container, Dialog, DialogActions, DialogContent, DialogContentText, DialogTitle, Drawer, Grid,
    IconButton, List, ListItem, ListItemButton, ListItemIcon, ListItemText, Snackbar, Tab, Tabs,
    TextField, Toolbar, Typography, useMediaQuery, useTheme
} from '@mui/material';
import MenuIcon from '@mui/icons-material/Menu';
import HomeIcon from '@mui/icons-material/Home';
import BarChartIcon from '@mui/icons-material/BarChart';
import PeopleIcon from '@mui/icons-material/People';
import SettingsIcon from '@mui/icons-material/Settings';
import NotificationsIcon from '@mui/icons-material/Notifications';


// --- Helper Components ---

function TabPanel(props) {
    const { children, value, index, ...other } = props;
    return (
        <div role="tabpanel" hidden={value !== index} id={`tabpanel-${index}`} aria-labelledby={`tab-${index}`} {...other}>
            {value === index && <Box sx={{ p: 3 }}>{children}</Box>}
        </div>
    );
}

function a11yProps(index) {
    return { id: `tab-${index}`, 'aria-controls': `tabpanel-${index}` };
}

// --- Benchmark Test Components ---

function Test1_UserProfileCard() {
    return (
        <Card sx={{ maxWidth: 345 }}>
            <CardMedia
                component="img"
                height="194"
                image="https://via.placeholder.com/345x194.png?text=User+Avatar"
                alt="User Avatar"
            />
            <CardContent sx={{ textAlign: 'center' }}>
                <Typography gutterBottom variant="h5" component="h2">
                    Jane Doe
                </Typography>
                <Typography variant="body2" color="text.secondary">
                    Lead Software Engineer
                </Typography>
            </CardContent>
            <CardActions sx={{ justifyContent: 'center', pb: 2 }}>
                <Button variant="contained" color="primary">Contact</Button>
            </CardActions>
        </Card>
    );
}

function Test2_ModalDialogForm() {
    const [open, setOpen] = useState(false);
    const handleClickOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);

    return (
        <div>
            <Button variant="contained" onClick={handleClickOpen}>
                Launch Contact Modal
            </Button>
            <Dialog open={open} onClose={handleClose}>
                <DialogTitle>Contact Us</DialogTitle>
                <DialogContent>
                    <DialogContentText>
                        Please fill out the form below and we will get back to you.
                    </DialogContentText>
                    <TextField autoFocus margin="dense" id="name" label="Name" type="text" fullWidth variant="standard" />
                    <TextField margin="dense" id="email" label="Email Address" type="email" fullWidth variant="standard" />
                    <TextField margin="dense" id="message" label="Message" type="text" fullWidth multiline rows={4} variant="standard" />
                </DialogContent>
                <DialogActions>
                    <Button onClick={handleClose}>Cancel</Button>
                    <Button onClick={handleClose} variant="contained">Send Message</Button>
                </DialogActions>
            </Dialog>
        </div>
    );
}

function Test3_AdvancedTabInterface() {
    const [mainTab, setMainTab] = useState(0);
    const [nestedTab, setNestedTab] = useState(0);
    const [loading, setLoading] = useState(false);
    const [profileContent, setProfileContent] = useState(null);

    const handleMainTabChange = (event, newValue) => {
        setMainTab(newValue);
    };

    const handleNestedTabChange = (event, newValue) => {
        setNestedTab(newValue);
    };

    useEffect(() => {
        if (mainTab === 1 && !profileContent) {
            setLoading(true);
            setTimeout(() => {
                setProfileContent({ name: 'John Smith', email: 'john.smith@example.com' });
                setLoading(false);
            }, 2000);
        }
    }, [mainTab, profileContent]);

    return (
        <Box sx={{ width: '100%' }}>
            <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
                <Tabs value={mainTab} onChange={handleMainTabChange} aria-label="main tabs">
                    <Tab label="Home" {...a11yProps(0)} />
                    <Tab label="Profile (Simulates Loading)" {...a11yProps(1)} />
                    <Tab label="Contact (With Nested Tabs)" {...a11yProps(2)} />
                </Tabs>
            </Box>
            <TabPanel value={mainTab} index={0}>
                This is the home tab content. It is simple and static.
            </TabPanel>
            <TabPanel value={mainTab} index={1}>
                {loading ? (
                    <Box sx={{ display: 'flex', justifyContent: 'center', p: 4 }}>
                        <CircularProgress />
                    </Box>
                ) : (
                    profileContent && (
                        <>
                            <Typography variant="h6">{profileContent.name}</Typography>
                            <Typography>{profileContent.email}</Typography>
                        </>
                    )
                )}
            </TabPanel>
            <TabPanel value={mainTab} index={2}>
                <Typography>This tab contains another set of tabs.</Typography>
                <Box sx={{ flexGrow: 1, bgcolor: 'background.paper', display: 'flex', mt: 2 }}>
                    <Tabs
                        orientation="vertical"
                        variant="scrollable"
                        value={nestedTab}
                        onChange={handleNestedTabChange}
                        aria-label="Nested tabs"
                        sx={{ borderRight: 1, borderColor: 'divider' }}
                    >
                        <Tab label="Work" {...a11yProps(0)} />
                        <Tab label="Personal" {...a11yProps(1)} />
                    </Tabs>
                    <TabPanel value={nestedTab} index={0}>Work contact info.</TabPanel>
                    <TabPanel value={nestedTab} index={1}>Personal contact info.</TabPanel>
                </Box>
            </TabPanel>
        </Box>
    );
}

function Test4_DashboardLayout() {
    const theme = useTheme();
    const isMobile = useMediaQuery(theme.breakpoints.down('md'));
    const [drawerOpen, setDrawerOpen] = useState(!isMobile);
    const drawerWidth = 240;

    const handleDrawerToggle = () => {
        setDrawerOpen(!drawerOpen);
    };

    const drawer = (
        <div>
            <Toolbar />
            <Box sx={{ overflow: 'auto' }}>
                <List>
                    {['Dashboard', 'Orders', 'Products', 'Customers'].map((text, index) => (
                        <ListItem key={text} disablePadding>
                            <ListItemButton>
                                <ListItemIcon>
                                    {index === 0 && <HomeIcon />}
                                    {index === 1 && <BarChartIcon />}
                                    {index === 2 && <PeopleIcon />}
                                    {index === 3 && <SettingsIcon />}
                                </ListItemIcon>
                                <ListItemText primary={text} />
                            </ListItemButton>
                        </ListItem>
                    ))}
                </List>
            </Box>
        </div>
    );

    return (
        <Box sx={{ display: 'flex', height: '500px', border: '1px solid #ccc', overflow: 'hidden' }}>
            <AppBar position="absolute" sx={{ zIndex: (theme) => theme.zIndex.drawer + 1 }}>
                <Toolbar>
                    <IconButton
                        color="inherit"
                        aria-label="open drawer"
                        edge="start"
                        onClick={handleDrawerToggle}
                        sx={{ mr: 2, display: { md: 'none' } }}
                    >
                        <MenuIcon />
                    </IconButton>
                    <Typography variant="h6" noWrap component="div">
                        Dashboard Co.
                    </Typography>
                </Toolbar>
            </AppBar>
            <Drawer
                variant={isMobile ? 'temporary' : 'permanent'}
                open={drawerOpen}
                onClose={handleDrawerToggle}
                sx={{
                    width: drawerWidth,
                    flexShrink: 0,
                    [`& .MuiDrawer-paper`]: { width: drawerWidth, boxSizing: 'border-box', position: 'relative' },
                }}
            >
                {drawer}
            </Drawer>
            <Box component="main" sx={{ flexGrow: 1, p: 3, bgcolor: 'grey.100' }}>
                <Toolbar />
                <Typography variant="h4" gutterBottom>Dashboard</Typography>
                <Grid container spacing={3}>
                    <Grid item xs={12} md={4}>
                        <Card>
                            <CardHeader title="New Users" />
                            <CardContent>
                                <Typography variant="h4">1,250</Typography>
                            </CardContent>
                        </Card>
                    </Grid>
                    <Grid item xs={12} md={4}>
                        <Card>
                            <CardHeader title="Sales" />
                            <CardContent>
                                <Typography variant="h4">$45,800</Typography>
                            </CardContent>
                        </Card>
                    </Grid>
                    <Grid item xs={12} md={4}>
                        <Card>
                            <CardHeader title="Pending Tasks" />
                            <CardContent>
                                <Typography variant="h4">17</Typography>
                            </CardContent>
                        </Card>
                    </Grid>
                </Grid>
            </Box>
        </Box>
    );
}

function Test5_SaaSApplicationPage() {
    const [drawerOpen, setDrawerOpen] = useState(true);
    const [settingsOpen, setSettingsOpen] = useState(false);
    const [toastOpen, setToastOpen] = useState(false);
    const drawerWidth = 240;

    const handleDrawerToggle = () => setDrawerOpen(!drawerOpen);
    const handleSettingsOpen = () => setSettingsOpen(true);
    const handleSettingsClose = () => setSettingsOpen(false);
    const handleToastOpen = () => setToastOpen(true);
    const handleToastClose = () => setToastOpen(false);

    return (
        <Box sx={{ display: 'flex', height: '600px', border: '1px solid #ccc', overflow: 'hidden' }}>
            <AppBar
                position="absolute"
                sx={{
                    width: `calc(100% - ${drawerOpen ? drawerWidth : 0}px)`,
                    ml: `${drawerOpen ? drawerWidth : 0}px`,
                    transition: (theme) => theme.transitions.create(['margin', 'width'], {
                        easing: theme.transitions.easing.sharp,
                        duration: theme.transitions.duration.leavingScreen,
                    }),
                }}
            >
                <Toolbar>
                    <IconButton color="inherit" edge="start" onClick={handleDrawerToggle} sx={{ mr: 2 }}>
                        <MenuIcon />
                    </IconButton>
                    <Typography variant="h6" noWrap sx={{ flexGrow: 1 }}>SaaS App</Typography>
                    <IconButton color="inherit" onClick={handleToastOpen}><NotificationsIcon /></IconButton>
                    <IconButton color="inherit" onClick={handleSettingsOpen}><SettingsIcon /></IconButton>
                </Toolbar>
            </AppBar>
            <Drawer
                sx={{
                    width: drawerWidth,
                    flexShrink: 0,
                    '& .MuiDrawer-paper': { width: drawerWidth, boxSizing: 'border-box', position: 'relative' },
                }}
                variant="persistent"
                anchor="left"
                open={drawerOpen}
            >
                <Toolbar />
                <List>
                    <ListItemButton><ListItemIcon><HomeIcon /></ListItemIcon><ListItemText primary="Dashboard" /></ListItemButton>
                    <ListItemButton><ListItemIcon><BarChartIcon /></ListItemIcon><ListItemText primary="Analytics" /></ListItemButton>
                </List>
            </Drawer>
            <Box
                component="main"
                sx={{
                    flexGrow: 1, p: 3, bgcolor: 'grey.100',
                    transition: (theme) => theme.transitions.create('margin', {
                        easing: theme.transitions.easing.sharp,
                        duration: theme.transitions.duration.leavingScreen,
                    }),
                    marginLeft: `-${drawerWidth}px`,
                    ...(drawerOpen && {
                        transition: (theme) => theme.transitions.create('margin', {
                            easing: theme.transitions.easing.easeOut,
                            duration: theme.transitions.duration.enteringScreen,
                        }),
                        marginLeft: 0,
                    }),
                }}
            >
                <Toolbar />
                <Typography paragraph>Main Workspace Content</Typography>
                <Grid container spacing={2}>
                    <Grid item xs={6}><Card><CardContent>Panel 1</CardContent></Card></Grid>
                    <Grid item xs={6}><Card><CardContent>Panel 2</CardContent></Card></Grid>
                </Grid>
            </Box>

            {/* Settings Modal */}
            <Dialog open={settingsOpen} onClose={handleSettingsClose}>
                <DialogTitle>User Settings</DialogTitle>
                <DialogContent>
                    <Typography>Configure your settings here.</Typography>
                </DialogContent>
                <DialogActions>
                    <Button onClick={handleSettingsClose}>Close</Button>
                </DialogActions>
            </Dialog>

            {/* Toast Notification */}
            <Snackbar
                open={toastOpen}
                autoHideDuration={4000}
                onClose={handleToastClose}
                message="Notification Received"
            />
        </Box>
    );
}


// --- Main Component to Render All Tests ---

export default function MaterialUIBenchmarkResults() {
    const tests = [
        { id: '1.1', title: 'User Profile Card', component: <Test1_UserProfileCard /> },
        { id: '2.1', title: 'Modal Dialog with Form', component: <Test2_ModalDialogForm /> },
        { id: '3.1', title: 'Advanced Tab Interface', component: <Test3_AdvancedTabInterface /> },
        { id: '4.1', title: 'Dashboard Page Layout', component: <Test4_DashboardLayout /> },
        { id: '5.1', title: 'Complete SaaS Application Page', component: <Test5_SaaSApplicationPage /> },
    ];

    return (
        <Container sx={{ py: 4 }}>
            <Typography variant="h3" component="h1" gutterBottom>
                Material-UI Benchmark Test Results
            </Typography>
            <Box component="main">
                {tests.map((test, index) => (
                    <Box key={test.id} component="section" sx={{ mb: 6 }}>
                        <Typography variant="h4" component="h2" gutterBottom>
                            Test {test.id}: {test.title}
                        </Typography>
                        <Card variant="outlined">
                            <CardContent>
                                {test.component}
                            </CardContent>
                        </Card>
                    </Box>
                ))}
            </Box>
        </Container>
    );
}

